
from bs4 import BeautifulSoup
import requests

# # HTML From File
# # with open("index.html", "r") as f:
# # 	doc = BeautifulSoup(f, "html.parser")

# # tags = doc.find_all("p")[0]

# # print(tags.find_all("b"))

# # HTML From Website
url = "https://www.fsmskills.in/user/profile.php?id=4384"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())
tags=doc.find_all("p") # it will print all the p tags in the doc and also shows  what inside of these p tags
print("tags",tags)
x = doc.find_all(string="source")
print("x",x)
# import mechanize
# from bs4 import BeautifulSoup
# import urllib2 
# import cookielib ## http.cookiejar in python3

# cj = cookielib.CookieJar()
# br = mechanize.Browser()
# br.set_cookiejar(cj)
# br.open("https://www.fsmskills.in/course/view.php?id=51")

# br.select_form(nr=0)
# br.form['username'] = 'username'
# br.form['password'] = 'password.'
# br.submit()

# print br.response().read()
# import requests
# from bs4 import BeautifulSoup

# login_url = 'https://www.fsmskills.in/my/'
# data = {
#     'username': 'nikita_sharma',
#     'password': 'write your own password'
# }

# with requests.Session() as s:
#     response = requests.post(login_url , data)
#     print(response.text)
#     index_page= s.get('https://www.fsmskills.in/my/')
#     soup = BeautifulSoup(index_page.text, 'html.parser')
#     print(soup.title)
# from bs4 import BeautifulSoup as bs 
# import requests 
# URL = "https://www.fsmskills.in/login/index.php" 
 
# payload = { 
# 	"uname": "nikita_sharma", 
# 	"pass": "write your own password" 
# } 
# s = requests.session() 
# response = s.post(URL, data=payload) 
# print(response.status_code) # If the request went Ok we usually get a 200 status. 
 
# from bs4 import BeautifulSoup 
# soup = BeautifulSoup(response.content, "html.parser") 
# protected_content = soup.find(attrs={"id": "pageName"}).text 
# print(protected_content)