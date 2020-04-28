from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys

import re

import json


search=sys.argv[1]
article_number=sys.argv[2]
article_num=int(article_number)
search=search.split(' ')

search='+'.join(search)

links_passed=set()
j=0
data = {}
data['bbc'] = []
#the news website we are searching
while(j<=30):
    j=j+1
    my_url="https://www.bbc.co.uk/search?q="
    my_url=my_url+search+'&page='+str(j)
    print(my_url)
    uClient = uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html5lib")
    
    
    div_tags=page_soup.find("div",{'class',"css-1vg3h2e-Stack e1y4nx260"})
    div_tags2=div_tags.find_all("div",{'class',"css-14rwwjy-Promo ett16tt11"})
    
    for i in div_tags2:
        try:
            div_tags3=i.find("div",{'class',"css-8d0yke-MetadataStripItem e1ojgjhb1"})
            date=div_tags3.dd.span.span.find_next_sibling().text
            print(date)
        except:
            div_tags4=div_tags3
            date=""
            continue
            
        div_tags4=div_tags3.find_next_sibling()
        category=div_tags4.span.text
        print(category)
        title_i=i.find("p",{'class',"css-1aofmbn-PromoHeadline ett16tt4"})
        title=title_i.span.text
        print(title)
        link=i.find('a').get('href')
        print(link)
        data['bbc'].append({
            'Title':title,
            'Date':date,
            'Category':category,
            'Link':link
        })
        links_passed.add(link)
        print(len(links_passed))
        if(len(links_passed)==article_num):
            break
        

    try:
        div_tags=page_soup.find("div",{"class","css-v574h-StyledContainer e1br8c160"})
        print(div_tags.p.text)
    except:
        pass
    else:
        break
    if (int(j)==30):
        break
    if(len(links_passed)==article_num):
        break
with open('sample.json', 'w') as outfile:
    json.dump(data, outfile)




