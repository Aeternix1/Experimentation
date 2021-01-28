from bs4 import BeautifulSoup

with open("ecologicalpyramid.html", "r") as ecological_pyramid: 
    soup = BeautifulSoup(ecological_pyramid, 'lxml') 

#find can be used to retrieve a variety of objects 

#search by tag
producer_entries = soup.find("ul")
print(producer_entries.li.div.string) 
print(type(producer_entries)) 

#search by text
string_find = soup.find(text="fox")
print(type(string_find)) 

#search by id 
primary_consumers = soup.find(id="primaryconsumers")
print(type(string_find))

#search based on customer attributes  
# customSoup.find(data-custom="custom")

#search based on the CSS class 
css_class = soup.find(class_= "primaryconsumerlist")
print(type(css_class))

#search using functions defined  
def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers' 

secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer) 

#search using methods in combination
plant_element = soup.find("div", class_="name")
print(plant_element) 

#find_all() will retrieve all the manifestations
secondary_consumer = soup.find_all(id="primaryconsumers")
print(secondary_consumer)
