from bs4 import BeautifulSoup
import requests 

source = requests.get('http://en.wikipedia.org/wiki/Yoel_Romero')

with open(source) as html_file: 
    soup = BeautifulSoup(html_file, 'lxml') 

print(soup.prettify())  

match = soup.title  

print(match) 

match = soup.p
print(match)


