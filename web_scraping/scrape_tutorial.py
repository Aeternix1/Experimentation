from bs4 import BeautifulSoup
import requests 

source = requests.get('http://

with open('test.html') as html_file: 
    soup = BeautifulSoup(html_file, 'lxml') 

print(soup.prettify())  

match = soup.title  

print(match) 

match = soup.p
print(match)


