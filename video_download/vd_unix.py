import os 
import sys 
import requests

single_dl = 'youtube-dl --ignore-errors --format best --output ' 
pl_dl = 'youtube-dl --ignore-errors -f best --output "%(title)s.%(ext)s" --yes-playlist '

#open the text file required
try:
    file = open(sys.argv[1], "r+")  
except IndexError:
    print("No file input")  
    exit()

Lines = file.readlines() 

videos = {}

for line in Lines:
    line = line.strip()
    if "https:" not in line: 
        title = '"' + line + '.%(ext)s"'
    else:  
        if "playlist" in line:
            tmp = " ".join([pl_dl, line.strip()])
        else: 
            tmp = " ".join([single_dl, title, line.strip()])
        os.system(tmp) 
        print(tmp) 
