#tagstojson: A Python module to retrieve all the links and the text about specified tag
#Author: Antonio Candela
#AKA: Delinet
#Twitter: @Delinet
#License: MIT 

import urllib2
import json
from bs4 import BeautifulSoup

def tagstojson(url,tag):
    response = urllib2.urlopen(url)
    html_doc = response.read()
    response.close()
    doc_by_soup = BeautifulSoup(html_doc)
    title = doc_by_soup.title.string

    #get all the links in the html_doc - method return a list of all 'a' tag(s)
    links = doc_by_soup.find_all('a',text=True)
    links_list = []
    if links:
        for link in links:
            links_list.append(str(link))
    #get all the tags == tag parameter in the html_doc - method return a list of all tag(s)
    tags = doc_by_soup.find_all(tag,text=True)
    tags_list=[]
    if tags:
        for tag in tags:
            tag_dict={}
            link_by_soup = BeautifulSoup(str(tag))
            tag_dict['tag_html'] = str(tag)
            tag_dict['tag_text'] = link_by_soup.get_text(strip=True)
            tags_list.append(tag_dict)

    #Start create the json file to return
    json_to_dump = {}
    json_to_dump['url'] = str(url)
    json_to_dump['title'] = title
    json_to_dump['links'] = links_list
    json_to_dump['tags'] = tags_list
    if tags_list:
        json_to_dump['error'] = 'false'
    else:
        json_to_dump['error'] = 'true'
    json_returned = json.dumps(json_to_dump, separators=(',', ': '))    
    #End create the json file to return
    
    return json_returned

    
        
if __name__=="__main__":
    json_obj = tagstojson('http://www.github.com','div')
    print json_obj
