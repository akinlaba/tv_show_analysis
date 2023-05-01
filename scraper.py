import requests
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import string
import re


# Xpath
part_1 = "//div[@class='lister-list']/div[@class='lister-item mode-advanced']["
part_2 = "]/div[@class='lister-item-content']/h3[@class='lister-item-header']/a/@href"
# url link to imdb search results
url_1 = "http://www.imdb.com/search/title?adult=include&countries=us&languages=en&num_votes=1000,&release_date=2005,&title_type=tv_series&user_rating=1.0,10&sort=user_rating,desc&view=advanced"
url_2 = "&page="
url_3 = "&ref_=adv_nxt"


# Webscrapping imdb movie_id list
id_list = []
for u in range(1, 29):
    URL = (url_1 + url_2 + str(u))
    r = requests.get(URL)
    HTML = r.text
    for i in range(1, 51):
        a_tag = Selector(text=HTML).xpath(part_1+str(i)+part_2).extract()
        for a in a_tag:
            id_list.append(a[7:16])

# Function to access the tv maze app, retrieve data and also accesses the imdb page to webscrape some more information
# converts data into dataframe
def get_movie_info(entry):
    res=requests.get('http://api.tvmaze.com/lookup/shows?imdb='+entry)
    if res.status_code == 200:
        results = json.loads(res.text)
        
        try:
            name = results['name']
        except TypeError:
            name = 'NaN'

        try:
            rating =  results['rating']['average']
        except TypeError:
            rating = 'NaN'

        try:
            genres = results['genres']
        except TypeError:
            genres = 'NaN'

        try:
            network = results['network']['name']
        except TypeError:
            network = 'NaN'

        try:
            premiered = results['premiered']
        except TypeError:
            premiered = 'NaN'

        try:
            status = results['status']
        except TypeError:
            status = 'NaN'

        try:
            types = results['type']
        except TypeError:
            types = 'NaN'
        
        try:
            show_id = results['id']
        except TypeError:
            show_id = 'NaN'
            
        url = "http://www.imdb.com/title/" + entry + "/reviews?ref_=tt_urv"
        r = requests.get(url)
        HTML = r.text
        path1 = "//div[@id='tn15content']/p["
        path2 = "]/text()"
        a_tag_list = []
        for i in range(1, 11):
            try:
                a_tag = Selector(text=HTML).xpath(path1 + str(i) + path2).extract()
                a_tag_list.append(a_tag[0])
            except:
                a_tag_list.append('NaN')
           
        res2 = requests.get('http://api.tvmaze.com/shows/' + str(show_id) + '/crew')
        crew_list_i = []
        if res2.status_code == 200:
            results2 = json.loads(res2.text)
            for number in range(len(results2)):
                try:
                    crew_list_i.append(results2[number]['person']['name'])
                except:
                    pass
        crew_set = set(crew_list_i)
        crew_list = list(crew_set)
        
        res3 = requests.get('http://api.tvmaze.com/shows/' + str(show_id))
        if res3.status_code == 200:
            results3 = json.loads(res3.text)
            
            try:
                summary = results['summary']
            except:
                summary = 'NaN'
            

        
        shows.loc[len(shows)] = [name, rating, genres, network, premiered, status, types, crew_list, summary, a_tag_list]

shows = pd.DataFrame(columns = ['show_name', 'rating_avg', 'genres', 'network', 'premiere_date', 'status', 'types', 'crew', 'summary', 'reviews'])

counter = 0
for entry in id_list:
    get_movie_info(entry)
    counter = counter + 1
    print counter

shows.to_pickle('shows.pkl')