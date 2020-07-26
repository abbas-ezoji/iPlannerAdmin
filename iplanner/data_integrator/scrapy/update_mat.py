# -*- coding: utf-8 -*-
import math
import requests
import numpy as np
import pyodbc
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, ForeignKey

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
    
update_need = pd.read_sql_query('''
                            SELECT [city_id]
                              ,[origin_id]
                              ,[origin_latt]
                              ,[origin_long]
                              ,[dest_id]
                              ,[dest_latt]
                              ,[dest_long]
                          FROM [planning].[dbo].[tehran_lost]
                          order by [city_id]
                              ,[origin_id]
									 
                                ''',
                       con=engine)
update_list = np.array(update_need.values)
dist_matrix = []
    
for t in update_list:
    city = int(t[0])
    orig_id = int(t[1])
    orig_latt = t[2]
    orig_long = t[3]
    print('city: ' + str(city) + ' from ' + str(orig_id) + ' to ' )
    
    dest_id = int(t[4])
    dest_latt = t[5]
    dest_long = t[6]
    print('dest: ' + str(dest_id))

    url = 'https://api.neshan.org/v2/direction?'
    apiKey = 'service.rstJXLArDfrfB3GG2iLd3i08trxmzNP1gjKd4lEI'
    origin = str(orig_latt) + ',' + str(orig_long)
    destin = str(dest_latt) + ',' + str(dest_long)

    url = url + 'origin=' + origin + '&destination=' + destin
    headers = {"Accept": "application/json", "Api-Key":apiKey}
    r = requests.get(url, headers = headers)
    data = r.json() 
    
    try:
        route = data.get('routes')[0]['legs'][0]
        len_time = route.get('duration')['value']//60
        len_meter = route.get('distance')['value']
        
        ecl_dist = math.sqrt((orig_latt-dest_latt)**2 + (orig_long-dest_long)**2)        
        destination_id = dest_id
        origin_id = orig_id
        travel_type_id = 1
        
        dist_matrix.append([ecl_dist, len_meter, len_time, 
                        origin_id, destination_id, 
                        travel_type_id, 'route'])
    except:
        dist_matrix.append([-1, -1, -1, 
                        orig_id, dest_id, 
                        1, ''])
    
    # query = '''update [plan_distance_mat]
    #            set ecl_dist = {}, len_meter = {}, len_time = {}, 
    #               travel_type_id = {}, route = {}
    #            where origin_id = {} and destination_id = {}
    #         '''.format(ecl_dist, len_meter, len_time, 
    #                    travel_type_id, "''",
    #                    origin_id, destination_id)        
    # with engine.connect() as con:
    #     con.execute(query)
        
print('insert into db for city: ' + str(city))
with engine.connect() as con:
    for i,d in enumerate(dist_matrix):
        query = '''insert into [plan_distance_mat] values({}, {}, {}, 
                                                    {}, {}, {}, {})
                '''.format(d[0], d[1], d[2], d[3], d[4], d[5], "''")
        con.execute(query)
        route_query = '''insert into [plan_dist_mat_routes] values({}, {}
                        , {}, {})
                '''.format("'"+str(d[6]).replace("'",'"')+"'", 0, d[3], d[4])
        con.execute(route_query)
print('finish')

