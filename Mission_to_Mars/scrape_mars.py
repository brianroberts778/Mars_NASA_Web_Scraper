#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Import Dependencies
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template
from splinter import Browser
from bs4 import BeautifulSoup as bs


# In[42]:


def init_browser():
    executable_path = {'chromedriver':'../Documents/chromedriver'}
    return Browser('chrome', executable_path, headless=False)


# In[43]:


def scrape_info():
    browser = init_broswer()
    final_dict = {}
    
    # Visit NASA Mars News Site 
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)
    html = browser.html
    news_soup = bs(html, "html.parser")
    
    # Scrape title and paragraph info
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text
    
    # Visit the JPL Mars Space Site and scrap featured images
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    html = browser.html
    img_soup = bs(html, "html.parser")
    
    # Scrape full size image link
    img_path = img_soup.find_all('img')[0]["src"]
    featured_img_url = jpl_url + img_path
    
    # Visit the Mars Facts webpage and scrape for facts including diameter, mass, etc.
    # Save these values in a HTML table string
    facts_url = "https://space-facts.com/mars/"
    facts_table = pd.read_html(facts_url)
    facts_df = facts_table[2]
    facts_df.columns = ["Variable","Value"]
    html_table = facts_df.to_html()
    html_table.replace('\n','')
    
    
    # Visit the USGS Astrology site to obtain high res. images for each of Mars' hemispheres
    # Links for each hemisphere are needed to find their respective images
    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_url)
    hemis_html = browser.html
    hemis_soup = bs(hemis_html,'html.parser')
    # Save both the image url string for the full resolution hemisphere image and...
    # ...the Hemisphere title containing the hemisphere name. Use a Python dictionary to...
    # store data and append the dict. with the img-url string and hemi title
    
    
    
    final_dict = {'news_title':news_title,
                 'news_p':news_p,
                 'featured_img_url':featured_img_url,
                 'fact_table':str(html_table)}
    
    return final_dict


# In[ ]:




