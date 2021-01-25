from bs4 import BeautifulSoup
import requests 

################### REQUESTS ################################################ 

# The parser keeps the markup  
# This is used to represent BeautifulSoup objects
helloworld = "<p> Hello World </p>"  
soup_string = BeautifulSoup(helloworld, 'lxml')   
print(soup_string) 

#We can also parse a file-like object using requests
url = 'https://en.wikipedia.org/wiki/Yoel_Romero'    
requests.get(url)
source = requests.get(url)
soup_req = BeautifulSoup(source.text, 'lxml')
# print(soup_req)  

######################  TAGS   ##############################################

html_atag = """<html>
<body><p>Test html a tag example </p>
<a href="http://www.packtpup.com">Home</a>
<a href="http://www.packtpup.com/books">Books</a>
</body>
</html>""" 
soup = BeautifulSoup(html_atag, 'lxml') 

#atag is an object containing all the data associated with the first <a> 
#within the object there are attributes that can be accessed such as: 
#class, id, href and style
atag = soup.a  
print(atag.attrs)  
print(atag['href'])   
#Printing the string value of the tag
print(atag.string)

#########################  FIND  ###########################################


