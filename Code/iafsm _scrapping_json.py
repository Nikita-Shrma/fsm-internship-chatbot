from bs4 import BeautifulSoup
import requests
import re
import json
from urllib.parse import urljoin

loginurl=('https://iafsm.in/index.php')
with requests.session() as s:
    def extract_content(element):
            content = ""
            for child in element.children:
                if child.name == "div":
                    content += extract_content(child)
                elif child.name in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "a"]:
                    content += child.get_text().strip() + " "
            return content.strip()

    r=s.get(loginurl) 
    #print(r.text)
    soup=BeautifulSoup(r.content,'html.parser')
    soup.encode("utf-8")

    div_elements = soup.find_all("div")

    # Prepare dictionary to store the content
    div_content = []

# Extract and store the content
    for div in div_elements:
        div_content.append(extract_content(div))

    # Create a dictionary for storing the content
    data = {
        "div_content": div_content,
        "heading_content": [heading.get_text() for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])],
        "p_content": [p.get_text() for p in soup.find_all("p")],
        "link_content": [link.get_text() for link in soup.find_all("a")]
    }

        # Convert the data dictionary to JSON format
    json_data = json.dumps(data, indent=4)
    filename = 'scraped_data.json'
    with open(filename, 'a') as file:
        file.write(json_data)
        
    links = soup.find_all('a') # searched for only a tags for navigating to other page
    print("links are: ")
    updated_link=set()
    internal_updated_link=set()
    for link in links:
        
        href = link.get('href')  # Use get() to safely retrieve the href attribute
         # if link is href and has only http 
        if href and "/index.php/" in href:
          absolute_url = urljoin("https://iafsm.in/", href)
          updated_link.add(absolute_url)
          #print(absolute_url) 
        if href and 'http' in href:
            #print('Link:', href)
            updated_link.add(href)
    for url in updated_link: 
          print("Link:-",url)  
          text1=s.get(url) # we use get() method again to scrap those links 
          soup1=BeautifulSoup(text1.content,'html.parser') # here parsed the data
          review=soup1.encode("utf-8")
          # soup1.prettify()
          #print(review)
          
        # Find all top-level <div> elements in the parsed HTML
          # Prepare dictionary to store the content
          # for div in div_elements:
          #     div_content.append(extract_content(div))

          # # Create a dictionary for storing the content
          # data = {
          #     "div_content": div_content,
          #     "heading_content": [heading.get_text() for heading in soup1.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])],
          #     "p_content": [p.get_text() for p in soup1.find_all("p")],
          #     "link_content": [link.get_text() for link in soup1.find_all("a")]
          # }


          # # Convert the data dictionary to JSON format
          # json_data = json.dumps(data, indent=4)
          # filename = 'scraped_data.json'
          # with open(filename, 'a') as file:
          #    file.write(json_data)
            ##


          internal_links = soup1.find_all('a') # searched for only a tags for navigating to other page
         
          
          for internal_link in internal_links:
              
              href = internal_link.get('href')  # Use get() to safely retrieve the href attribute
              # if link is href and has only http 
              if href and "/index.php/" in href:
                internal_absolute_url = urljoin("https://iafsm.in/", href)
                internal_updated_link.add(internal_absolute_url)
                #print(absolute_url) 
              if href and 'http' in href:
                  #print('Link:', href)
                  internal_updated_link.add(href)
    for internal_url in internal_updated_link: 
         
          print("internal_link=",internal_url)  
          internal_text1=s.get(internal_url) # we use get() method again to scrap those links 
          soup2=BeautifulSoup(internal_text1.content,'html.parser') # here parsed the data
          internal_review=soup2.encode("utf-8")
          
          
          div_elements = soup2.find_all("div")

        
# Extract and store the content
          # for div in div_elements:
          #     div_content.append(extract_content(div))

          # # Create a dictionary for storing the content
          # data = {
          #     "div_content": div_content,
          #     "heading_content": [heading.get_text() for heading in soup2.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])],
          #     "p_content": [p.get_text() for p in soup2.find_all("p")],
          #     "link_content": [link.get_text() for link in soup2.find_all("a")]
          # }
          # # Convert the data dictionary to JSON format
          # json_data = json.dumps(data, indent=4)
          # filename = 'scraped_data.json'
          # with open(filename, 'a') as file:
          #   file.write(json_data)
                # soup1.prettify()
                #print(internal_review)



          # internal_links=soup1.find_all('a') # now wrt each link we scrape he data and all the links on each page 
          #                                     # are scraped out
          # for internal_link in internal_links:
          #     href1=internal_link.get('href')
          #     if href  :
          #         internal_link_text=s.get(href)
                  
          #         soup2=BeautifulSoup(internal_link_text.content,'html.parser')
          #         review_internal=soup2.encode("utf-8")
          #         print(review_internal)
          