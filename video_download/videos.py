import os 
import sys

single_dl = 'C:\youtube-dl\youtube-dl.exe --ignore-errors --format best --output ' 
multiple_dl = 'C:\youtube-dl
#open the text file required
file = open(sys.argv[1])
Lines = file.readlines() 

videos = {}

for line in Lines:
    line = line.strip()
    if "https:" not in line:
        out = '"' + line + '.%(ext)s"' 
    else if "playlist"
    else:
        tmp = " ".join([cmd_string, out, line.strip()])
        os.system(tmp) 
        #print(tmp)
