
from bs4 import BeautifulSoup

# read from html file in local directory
# with open("random html.html","r") as f:
#     doc=BeautifulSoup(f,"html.parser")
# print (doc.prettify())# print the file in html format only readable and new lines

# search  by tags
# tag=doc.title
# print(tag) # o/p  <title>Your Title Here</title>
# print(tag.string) # o/p Your Title Here

# modify the tag
# tag.string="hello"
# print(tag) #<title>hello</title> 

# tags=doc.find_all("p") # it will print all the p tags in the doc and also shows  what inside of these p tags
# print(tags)
# now search for nested tags
tagss=doc.find_all("p")[0] #print 1st p tag 
print("tagss=",tagss)
tag=doc.find("p")
print("tags=",tag)
 
tag1=tagss.find_all("b")
print(tag1)


# read from website.
