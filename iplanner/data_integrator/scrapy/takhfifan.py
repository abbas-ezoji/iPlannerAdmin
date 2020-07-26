# -*- coding: utf-8 -*-
import pyodbc
import json

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, ForeignKey
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime  
from dateutil.relativedelta import relativedelta

USER = 'sa'
PASSWORD = 'xZCtQxjK3z9A'
HOST = '185.10.72.91,1886'
PORT = '1433'
NAME = 'iPlannerWebApi_new'
engine = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver=SQL+Server' \
                       .format(USER,
                               PASSWORD,
                               HOST,
                               NAME
                               ))
    
cities = {116:'tehran',136:'mashhad',71:'isfahan',73:'karaj',361:'kish',
          296:'rasht',1:'tabriz'}
categories = {6:'restaurants-cafes'} #'recreational-sports', 'recreational-sports'education art-culture beauty-cosmetics services

for city_key, city in cities.items():   
    print('City: ' + city)
    for category_key, category in categories.items(): 
        print('category: ' + category)
        offset = 0
        limit = 33
        url = "https://takhfifan.com/v4/api/magento/products?" + \
            f"filters[category]={category}&filters[city]={city}&limit={limit}&offset={offset}&"
        while True:
            r = requests.get(url)
            data_str = r.text
            
            data_json = json.loads(data_str)
            data = data_json.get('data')
            if len(data)==0:
                break
            meta_data = data_json.get('meta')
            
            for d in data:
                ExternalId = d.get('id')
                
                data_attrs = d.get('attributes')
                
                Lang = 0
                TotalDealQuantity = 0    
                UsageDeadline = 0
                Description = '-'
                Point = 0
                VisitDuration = 0
                VisitTimeFrom = 0
                VisitTimeTo = 0
                MyProperty = 0
                VisitDateFrom = datetime.now()
                VisitDateTo = VisitDateFrom + relativedelta(years=1)
                
                if data_attrs.get('short_title'):
                    Title = data_attrs.get('short_title')
                    
                if data_attrs.get('UrlKey'):
                    BaseUrl = 'https://takhfifan.com/deal/'
                    UrlKey = data_attrs.get('url_key')
                    BaseUrl += f'{ExternalId}/{UrlKey}'
                else:
                    UrlKey = BaseUrl = '-'
                    
                if data_attrs.get('image'):
                    Image = data_attrs.get('image')
                else:
                    Image = '-'
                
                if data_attrs.get('name'):
                    FullTitle = data_attrs.get('name')
                    EnglishTitle = 'en'
                else:
                    FullTitle = EnglishTitle = '-'
                
                if data_attrs.get('vendor'):
                    area = data_attrs.get('area') if data_attrs.get('area') else '-'
                    district = data_attrs.get('district') if data_attrs.get('district') else '-'
                    Address = area + district
                else:
                    Address = '-'
                    
                if data_attrs.get('price_regular'):
                    RegularPrice = data_attrs.get('price_regular')
                    DealPrice = data_attrs.get('price_deal') if data_attrs.get('price_deal') else 0
                    DealDiscount = data_attrs.get('deal_discount') if data_attrs.get('deal_discount') else 0
                else:
                    RegularPrice = DealPrice = DealDiscount = 0
                
                if data_attrs.get('deal_qty_sold'):
                    SoldDealQuantity = data_attrs.get('deal_qty_sold')
                else:
                    SoldDealQuantity = 0
                
                Lat = data_attrs.get('latitude') if data_attrs.get('latitude') else 0    
                Long = data_attrs.get('longtitude') if data_attrs.get('longtitude') else 0
                try:    
                    Lat = float(Lat)
                    Long = float(Long)
                except:
                    Lat = Long = 0    
                
                if data_attrs.get('vendor_rate'):
                    Rate = data_attrs.get('vendor_rate')
                else: 
                    Rate = 0
                    
                Active = 1 if data_attrs.get('can_use_now') else 0
                
                ExternalProductId = data_attrs.get('protuct_id') if data_attrs.get('protuct_id') else 0
                CityId = 1
                SubCategoryId = 1
                CategoryId = 1
                iPlannerRate = 0
                UserRate = Rate
                with engine.connect() as con:
                    query = '''INSERT INTO Event
                        	([Lang]
                        	,[Title]
                        	,[UrlKey]
                        	,[BaseUrl]
                        	,[Image]
                        	,[FullTitle]
                        	,[EnglishTitle]
                        	,[Address]
                        	,[RegularPrice]
                        	,[DealPrice]
                        	,[DealDiscount]
                        	,[SoldDealQuantity]
                        	,[TotalDealQuantity]
                        	,[UsageDeadline]
                        	,[Description]
                        	,[Lat]
                        	,[Long]
                        	,[Point]
                        	,[VisitDuration]
                        	,[VisitTimeFrom]
                        	,[VisitTimeTo]
                        	,[VisitDateFrom]
                        	,[VisitDateTo]
                        	,[Rate]
                        	,[Active]
                        	,[MyProperty]
                        	,[ExternalId]
                        	,[ExternalProductId]
                        	,[CityId]
                        	,[SubCategoryId]
                        	,[CategoryId]
                        	,[iPlannerRate]
                        	,[UserRate])
                        VALUES({}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{}
                              ,{})
                        '''.format(Lang
                              ,"'" + Title + "'"
                              ,"'" + UrlKey + "'"
                              ,"'" + BaseUrl + "'"
                              ,"'" + Image + "'"
                              ,"'" + FullTitle + "'"
                              ,"'" + EnglishTitle + "'"
                              ,"'" + Address + "'"
                              ,RegularPrice
                              ,DealPrice
                              ,DealDiscount
                              ,SoldDealQuantity
                              ,TotalDealQuantity
                              ,UsageDeadline
                              ,"'" + Description + "'"
                              ,Lat
                              ,Long
                              ,Point
                              ,VisitDuration
                              ,VisitTimeFrom
                              ,VisitTimeTo
                              ,"'" + str(VisitDateFrom) + "'" 
                              ,"'" + str(VisitDateTo) + "'" 
                              ,Rate
                              ,Active
                              ,MyProperty
                              ,ExternalId
                              ,ExternalProductId
                              ,CityId
                              ,SubCategoryId
                              ,CategoryId
                              ,iPlannerRate
                              ,UserRate)
                
                    con.execute(query)
                    print('ExternalId: ' + str(ExternalId))
                
            offset += limit
            print('offset: ' + str(offset))