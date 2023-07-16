
from bs4 import BeautifulSoup
import requests
import re
import json
from urllib.parse import urljoin

loginurl=('https://iafsm.in/index.php')

with requests.session() as s:
    
    # we extract the link and parsed it   
    r=s.get(loginurl) 
    #print(r.text)
    soup=BeautifulSoup(r.content,'html.parser')
    soup.encode("utf-8") # converted to utf-8 as initial encoding was iso
    
    data = {"div_content": [], "p_content": []}
    div_elements=soup.find_all("div",class_="sppb-addon-content")
    for div in div_elements:
        data["div_content"].append(div.get_text())
   
    
    p_elements=soup.find_all("p")
    for p in p_elements:
        data["p_content"].append(p.get_text())
   

    # searched for only a tags for navigating to other page   
    links = soup.find_all('a') 
    print("links are: ")
    updated_link=set() # set is created to prevent repeating of links.
    internal_updated_link=set() #this is set containing links eg. dashboard->technologies->youtube link(on technology page)
    
    #iterating all the links on home page
    for link in links:
        href = link.get('href')  #  retrieve only the href attribute
        if href and "/index.php/" in href: #if links are href and strating with index.php 
          absolute_url = urljoin("https://iafsm.in/", href) # we will add this pattrn inorder to make navigable links
          updated_link.add(absolute_url) #stored them in set
          #print(absolute_url) 

        if href and 'http' in href: # also stored href link which are http 
            #print('Link:', href)
            updated_link.add(href)

    # now iterating all the links on home page        
    for url in updated_link: 
        print("Link:-",url)  
        text1=s.get(url) # we use get() method again to scrap those home page links 
        soup1=BeautifulSoup(text1.content,'html.parser') # here parsed the data
        review=soup1.encode("utf-8")
        
        linked_div_elements=soup1.find_all("div",class_="sppb-addon-content")
        for div in linked_div_elements:
            data["div_content"].append(div.get_text())
            #individual_data["div_content"].append(div.get_text())
        linked_p_elements=soup1.find_all("p")
        for p in linked_p_elements:
            data["p_content"].append(p.get_text())
            
          #now links on home page have other links like technlogy have videos, documentaitons' links 
        internal_links = soup1.find_all('a') # searched for only a tags for navigating to other page
        for internal_link in internal_links:
            
            href = internal_link.get('href')  #  retrieved the href attribute links
            if href and "/index.php/" in href: #if links are href and starting with index.php 
                internal_absolute_url = urljoin("https://iafsm.in/", href) # we will add this pattrn inorder to make navigable links
                internal_updated_link.add(internal_absolute_url) # stored them in another set
                #print(absolute_url) 
                if href and 'http' in href: # if links are href and http
                    #print('Link:', href)
                    internal_updated_link.add(href) # stored them in set

    #iterated internal_updated_link               
    for internal_url in internal_updated_link: 
        print("internal_link=",internal_url)  
        internal_text1=s.get(internal_url) # we use get() method again to scrap those links 
        soup2=BeautifulSoup(internal_text1.content,'html.parser') # here parsed the data
        internal_review=soup2.encode("utf-8")
        
        
   
        internal_linked_div_elements=soup2.find_all("div",class_="sppb-addon-content")
        for div in internal_linked_div_elements:
            data["div_content"].append(div.get_text())
           
        
        internal_linked_p_elements=soup2.find_all("p")
        for p in p_elements:
            data["p_content"].append(p.get_text())
           
    json_data = json.dumps(data, indent=4)
    filename = 'website_data.json'
    with open(filename, 'a') as file:
        file.write(json_data)

