from bs4 import BeautifulSoup
import requests 

url = 'https://en.wikipedia.org/wiki/Yoel_Romero'
source = requests.get(url)        
#Requests has an attribute containing text
data = source.text
soup = BeautifulSoup(data, 'lxml') 

match = soup.find("table")
# print(match.prettify()) 

#find(name, attrs, recursive, text, **kwargs)
rows = match.find_all(name="tr") 
for row in rows: 
    print(row.text.strip())

