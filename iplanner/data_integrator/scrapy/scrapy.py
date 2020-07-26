# -*- coding: utf-8 -*-

import pyodbc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, ForeignKey
import requests
from bs4 import BeautifulSoup
import pandas as pd

USER = 'sa'
PASSWORD = 'xZCtQxjK3z9A'
HOST = '185.10.72.91,1886'
PORT = '1433'
NAME = 'planning'
engine = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver=SQL+Server' \
                       .format(USER,
                               PASSWORD,
                               HOST,
                               NAME
                               ))

df_city = pd.read_sql_query('''SELECT [id]
                                          ,[name]
                                          ,[phoneCode]
                                          ,[latt]
                                          ,[long]
                                          ,[province_id]
                                          ,[safarzoon_id]
                                    FROM [safarzoon_city]
                                    WHERE ID NOT IN (SELECT city_id FROM 
                                                     safarzoon_attraction)
                                    ''',
                       con=engine)

for c_i, c in enumerate(df_city.values):
    country_id = 98
    province_id = c[5]
    city_id = c[0]
    base_url = 'https://safarzon.com/attractionSearch?page={}&countries%5B%5D=98&provinces%5B%5D=' + \
               str(province_id) + \
               '&cities%5B%5D=' + str(city_id) +'&search_name='
    print(base_url)
    
    attr_list = []
    i = 1
    while True:
        attrs_url = base_url.format(i)
        r = requests.get(attrs_url)
        r = r.json()['data']
        if not r:
            break
        attr_list.append(r)
        i += 1
    
    if not attr_list:
        continue
    rows = len(attr_list)
    cols = len(attr_list[0])    
    cols_of_last_row = len(attr_list[-1])
    attr_count = ((rows-1 if rows>1 else 0) * (cols)) + cols_of_last_row
    
    data = []
    for r in range(rows):
        for c in range(cols):
            url = 'https://safarzon.com/attractions/'
            if r == rows-1 and c==cols_of_last_row:
                break
            _id = attr_list[r][c]['id']
            title = attr_list[r][c]['title']
            image = attr_list[r][c]['image']
            url +=  _id
            print(url)
            
            res_staus = 0
            try:
                res = requests.get(url, timeout=10)
                res_staus = 1
            except:
                d = [int(_id), title, 
                     '', '', '', '', '', '',
                     0, 0, image]
                data.append(d)
                
            if res_staus == 0:
                continue
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')

            full_title = soup.find('h1', {"class": "text-right h1toh4"})
            full_title = full_title.text

            properties = soup.find_all('div', {"class": "attraction-properties"}) 
            rq_time = properties[0].find_all('span')[1].text
            vis_time = properties[1].find_all('span')[1].text
            address = properties[2].find_all('span')[1].text
            cost = properties[3].find_all('span')[1].text

            describtion = soup.find('div', {"class": "container attraction-caption"})
            describtion = describtion.find('p')
            describtion = describtion.text if describtion is not None else ''

            location = soup.find('div', {"class": "col-lg-12 text-center d-block d-md-none order-2 mt-3 mb-3"})
            location = location.find('a').get('href')

            view = soup.find('span', {"class": "p-1"})
            like = soup.find('span', {"class": "p-2"})
            view_count = int(view.find('span').text if view is not None else 0)
            like_count = int(like.find('span').text if like is not None else 0)

            d = [int(_id), title, full_title, address, 
                 cost, describtion, rq_time, vis_time, 
                 like_count, view_count,
                 image, location]
            data.append(d)
            
    with engine.connect() as con:
        for i,d in enumerate(data):
            query = '''INSERT INTO safarzoon_attraction
                                      ([type]
                                      ,[phoneCode]
                                      ,[title]
                                      ,[fullTitle]
                                      ,[address]
                                      ,[cost]
                                      ,[description]
                                      ,[latt]
                                      ,[long]
                                      ,[rq_time]
                                      ,[vis_time]
                                      ,[vis_time_from]
                                      ,[vis_time_to]
                                      ,[like_no]
                                      ,[view_no]
                                      ,[image]
                                      ,[city_id]
                                      ,[country_id]
                                      ,[province_id]
                                      ,[safarzoon_id]
                                      ,[location]) 
                        VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, 
                                {}, {}, {}, {}, {}, {}, {}, {}, {})
                        '''.format(0, 0, "'" + d[1] + "'", "'"+d[2]+"'", "'"+d[3]+"'", "'"+d[4]+"'", 
                            "'"+ d[5].replace("'", " ")+"'",
                                   0, 0, "'"+d[6]+"'", "'"+d[7]+"'",0,0, d[8], d[9], "'"+d[10]+"'", 
                                  city_id, country_id, province_id, d[0], "'"+d[11]+"'")
            # print(query)
            con.execute(query)
        print('inserted ----')
    
    