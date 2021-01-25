from bs4 import BeautifulSoup
import requests 

#This is a string formatted in HTML
helloworld = "<p> Hello World </p>" 
soup_string = BeautifulSoup(helloworld, 'lxml')  

#We can also parse a file-like object
url = 'https://en.wikipedia.org/wiki/Yoel_Romero'    

#requests.get(url) retrieves all the data associated with a request 
#the text object contains the .html file
source = requests.get(url)    
# print(source.text)

#BeautifulSoup requires a .html file to be parsed
soup_file = BeautifulSoup(source.text, 'lxml')


#The parsed value contains all of the formatting and uses it
#The markup is used to represent BeautifulSoup objects
print(soup_string) 
print(soup_file)
