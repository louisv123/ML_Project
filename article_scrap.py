import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import datetime
import time

from bs4 import BeautifulSoup

from selenium import webdriver
path_to_chromedriver = '/Users/Louis/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://blog.oceanprotocol.com/from-enterprise-decentralization-to-tokenization-and-beyond-abeaab786e14'
browser.get(url)
soup=BeautifulSoup(browser.page_source,"html.parser")


###title############################

#get article title and return into string
def get_title(browser):
    return browser.find_element_by_css_selector(".graf.graf--h3.graf--leading.graf--title").text



#####clap########################
#get number of clap (int)
def get_clap(browser):
    clap=browser.find_element_by_css_selector(".button.button--chromeless.u-baseColor--buttonNormal.js-multirecommendCountButton.u-block.u-marginAuto").text
    
    if clap[-1]=='K':
        clap=clap[:-1]+'00'
    clap=clap.replace(".", "")
    return int(clap)

###comment############################
#get number of comment (int)
def get_comment(browser):
    comment=browser.find_element_by_css_selector('.buttonSet.u-flex0').text
    if comment[-1]=='K':
        comment=comment[:-1]+'00'
    return int(comment.replace(".", ""))
   
    
    
######tags#######################################
#get list of tags and count it list(list(string),int)
def get_tags(browser):
    html_list = browser.find_element_by_css_selector('.tags.tags--postTags.tags--borderless')
    items = html_list.find_elements_by_tag_name("li")
    list_tag=list()
    tag=list()
    for item in items:
        tag.append(item.text)
    return [tag,len(tag)]

#####minutes read #################################
#get minute read (int)
def get_minute_read(browser):
    soup=BeautifulSoup(browser.page_source,"html.parser")
    min_read=soup.find("span", class_="readingTime")['title'].encode('utf-8')
    return int(str.rsplit(min_read)[0])


######date posted #############################
#get date when article has been posted (time : yy, mm, dd)
def get_date(browser):
    soup=BeautifulSoup(browser.page_source,"html.parser")
    date_post=soup.find("time")['datetime'].encode('utf-8')
    date_post=str.rsplit(date_post,"-")
    day=str.rsplit(date_post[-1],"T")
    date_post[-1]=day[0]
    return time.strptime(date_post[0]+" "+date_post[1]+" "+date_post[2] , "%Y %m %d") 

######text features###########################################
#get number of paragraph (p), number of figure (image), number of bullet point (li) = list(int,int,int)
def get_text_features(browser):
    soup=BeautifulSoup(browser.page_source,"html.parser")
    carac_article_html=soup.find("div",class_="section-inner sectionLayout--insetColumn")
    return [len(carac_article_html.find_all("p")),len(carac_article_html.find_all("figure")),len(carac_article_html.find_all("li"))]