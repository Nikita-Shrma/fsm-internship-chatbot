
from bs4 import BeautifulSoup
import requests
import re
import credential
import json


loginurl=('https://www.fsmskills.in/login/index.php')
secure_url=('https://www.fsmskills.in/my/')


with requests.session() as s:
    r=s.get(loginurl)  # used get method in order to extract logintoken

    req=r.text
    pattern = r'<input type="hidden" name="logintoken" value="(.*?)"' #
    match = re.search(pattern, r.text) #SEARCH FOR pattern in the text 

    if match:
        desired_value = match.group(0)  # if math is true then value get stored in dersired_value
    else:
     desired_value = None
    print(desired_value)
    value=[]
    for i in range(46,len(desired_value)-1):  # here exact login token value got traversed 
        str2=desired_value[i]   # and stored in str2
        value.append(str2)      # appended in variable named value in list format 
    #print(value)
    str_value=""
    final_token=str_value.join(value)   # here value get converted to string
    #print(final_token)
    payload1={
        'logintoken':final_token,
        'username':credential.username,  # called another file for username and password which stores information
        'password':credential.password,
        'rememberusername':'1'
    }
    r2=s.post(loginurl, data =payload1)  # here post method is used to login into website 
    
    r3=s.get(secure_url)  # once logging in we scrape dashboard of website
    print(r2.text)
   
   
    soup=BeautifulSoup(r3.content,'html.parser',)
    soup.encode("utf-8")  # convrted to utf-8 as encoding is something else
    #print(soup.prettify("utf-8"))
    name=[tag.name for tag in soup.find_all()]
    print(name)
    #print(soup.prettify("utf-8"))
    for i in name:
        title_element = soup.find(name=i)  # Find the <title> element
        title = title_element.text.strip() if title_element else ""

        tag_content = soup.find_all(i)  # Find all <p> elements
        content = [p.text.strip() for p in tag_content] if tag_content else []

        # Organize the extracted information in a data structure
        data = {
             i: title,
            'content': content
        }

        # Convert the data to JSON format
        json_data = json.dumps(data, indent=4)

        # Write the JSON data to a file
        filename = 'scraped_data.json'
        with open(filename, 'a') as file:
            file.write(json_data)

    print(f"Scraped data has been stored in {filename} successfully.")
    
    links = soup.find_all('a') # searched for only a tags for navigating to other page
    print("links are: ")
    for link in links:
        href = link.get('href')  # Use get() to safely retrieve the href attribute
        if href and 'http' in href: # if link is href and has only http  
            print('Link:', href)  #then we print the links

            text1=s.get(href) # we use get() method again to scrap those links 
            #print(text1.text)
            
            soup1=BeautifulSoup(text1.content,'html.parser') # here parsed the data
            soup1.encode("utf-8")
            dashboard_link_page=[tag.name for tag in soup.find_all()]
            print(dashboard_link_page)
            for i in dashboard_link_page:
                dashboard_link_page_element = soup.find(dashboard_link_page=i)  # Find the <title> element
                dashoboard_linked_page = dashboard_link_page_element.text.strip() if dashboard_link_page_element else ""

                tag_content_ele = soup.find_all(i)  # Find all <i> elements
                dashoboard_linked_page_content = [p.text.strip() for p in tag_content_ele] if tag_content_ele else []

                # Organize the extracted information in a data structure
                data = {
                    i: dashoboard_linked_page,
                    ' dashoboard_linked_page_content ': dashoboard_linked_page_content
                }

                # Convert the data to JSON format
                json_data = json.dumps(data, indent=4)

                # Write the JSON data to a file
                filename = 'scraped_data.json'
                with open(filename, 'a') as file:
                    file.write(json_data)
           
            internal_links=soup1.find_all('a') # now wrt each link we scrape he data and all the links on each page 
                                               # are scraped out
            for internal_link in internal_links:
                href1=internal_link.get('href')
                if href1 and 'http' in href1 :
                    internal_link_text=s.get(href)
                    #print(internal_link_text.text)
                    
                    soup2=BeautifulSoup(internal_link_text.content,'html.parser')
                    soup2.encode("utf-8")
                    internal_links_name=[tag.name for tag in soup.find_all()]
                    print(internal_links_name)
                    #print(soup.prettify("utf-8"))
                    for i in internal_links_name:
                        internal_links_name_element = soup.find(internal_links_name=i)  # Find the <title> element
                        internal_links_name_element_title = internal_links_name_element.text.strip() if internal_links_name_element else ""

                        internal_links_name_tag_content = soup.find_all(i)  # Find all <p> elements
                        internal_links_name_content = [p.text.strip() for p in internal_links_name_tag_content] if internal_links_name_tag_content else []

                        # Organize the extracted information in a data structure
                        data = {
                            i: internal_links_name_element_title,
                            'content': internal_links_name_content
                        }

                        # Convert the data to JSON format
                        json_data = json.dumps(data, indent=4)

                        # Write the JSON data to a file
                        filename = 'scraped_data.json'
                        with open(filename, 'a') as file:
                            file.write(json_data)
            
    # for i in range(0,len(link)):
    #    r=s.get(link[i])
    #    print("r=",r.text)
    # import httplib2
    # from bs4 import BeautifulSoup, SoupStrainer

    # http = httplib2.Http()
    # status, response = http.request('https://www.fsmskills.in/my/')

    # for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    #     if link.has_attr('href'):
    #         print(link['href'])

  