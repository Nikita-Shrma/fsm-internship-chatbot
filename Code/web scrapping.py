
from bs4 import BeautifulSoup
import requests
import re
import credential

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
    r3=s.post(loginurl, data =payload1)  # here post method is used to login into website 
    
    r2=s.get(secure_url)  # once logging in we scrape dashboard of website
    print(r2.text)
    soup=BeautifulSoup(r2.content,'html.parser',)
    soup.encode("utf-8")  # convrted to utf-8 as encoding is something else
    #print(soup.prettify("utf-8"))
    
    links = soup.find_all('a') # searched for only a tags for navigating to other page
    print("links are: ")
    for link in links:
        href = link.get('href')  # Use get() to safely retrieve the href attribute
        if href and 'http' in href: # if link is href and has only http  
            print('Link:', href)  #then we print the links

            text1=s.get(href) # we use get() method again to scrap those links 
            print(text1.text)
            soup1=BeautifulSoup(text1.content,'html.parser') # here parsed the data
            soup1.encode("utf-8")
            internal_links=soup1.find_all('a') # now wrt each link we scrape he data and all the links on each page 
                                               # are scraped out
            for internal_link in internal_links:
                href1=internal_link.get('href')
                if href1 and 'http' in href1 :
                    internal_link_text=s.get(href)
                    print(internal_link_text.text)
                    soup2=BeautifulSoup(internal_link_text.content,'html.parser')
                    soup2.encode("utf-8")
            
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

  