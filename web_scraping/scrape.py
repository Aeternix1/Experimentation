from bs4 import BeautifulSoup
import requests  
import sys

################### REQUESTS ################################################ 

# # The parser keeps the markup  
# # This is used to represent BeautifulSoup objects
# helloworld = "<p> Hello World </p>"  
# soup_string = BeautifulSoup(helloworld, 'lxml')   
# print(soup_string) 

# #We can also parse a file-like object using requests
# url = 'https://en.wikipedia.org/wiki/Yoel_Romero'    
# requests.get(url)
# source = requests.get(url)
# soup_req = BeautifulSoup(source.text, 'lxml')
# # print(soup_req)  

# ######################  TAGS   ##############################################

# html_atag = """<html>
# <body><p>Test html a tag example </p>
# <a href="http://www.packtpup.com">Home</a>
# <a href="http://www.packtpup.com/books">Books</a>
# </body>
# </html>""" 
# soup = BeautifulSoup(html_atag, 'lxml') 

# #atag is an object containing all the data associated with the first <a> 
# #within the object there are attributes that can be accessed such as: 
# #class, id, href and style
# atag = soup.a  
# print(atag.attrs)  
# print(atag['href'])   
# #Printing the string value of the tag
# print(atag.string) 


##Exercise : Print the title and summary of Yoel Romero's wikipedia Page
# url = 'https://en.wikipedia.org/wiki/Yoel_Romero'
# requests.get(url)
# source = requests.get(url)
# soup = BeautifulSoup(source.text, 'lxml') 

# title = soup.h1 
# # print(title.attrs)
# print(title.text) 

# summary = soup.p
# print(summary.text)

# Exercise : Loop through multiple fighters and retrieve the title + wiki
# Exercise : Retrieve the Win/Loss Table of a fighter 

# summary + summary table
wiki_url = 'https://en.wikipedia.org/wiki/' 
# fighters = ["Yoel Romero", "Dustin Poirier", "Connor McGregor"]    
fighters = ["Yoel Romero"]

#Output file
with open("fighters.txt", 'w') as f: 
    sys.stdout = f

    # Given a fighter name, produce it's wikipedia URL
    for fighter in fighters: 
        tmp = fighter.split()
        fighter = "_".join(tmp)   
        url = wiki_url + fighter  
        
        #Parse the URL and access the heading, table and opening summary paragraph
        requests.get(url)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        title = soup.h1
        print(title.text)
        tables = soup.find_all("table") 
        for x in range(0, len(tables)): 
            if "Professional record breakdown" in tables[x].text:
                wl_record = tables[x]
                p_record = tables[x + 1]

        # print(wl_record.text) 
        tables = [wl_record, p_record]   

        for table in tables:
            t_entries = table.find_all("td")
            for entry in t_entries:
                print(entry.text.strip())

        # #Print off the tr and th
        # for x in range(0, 20): 
            # print(table_heading[x].text)
            # print(table_value[x+1].text) 
            
    
    # print(table_heading)  
    # print(table_value)
    # Need consistent formatting to scrape without introducing exception logic 

