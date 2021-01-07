import os 
import sys

cmd_string = 'C:\youtube-dl\youtube-dl.exe --ignore-errors --format best --output '
#open the text file required
file = open(sys.argv[1])
Lines = file.readlines() 

videos = {}

for line in Lines:
    line = line.strip()
    if "https:" not in line:
        out = '"' + line + '.%(ext)s"'
    else:
        tmp = " ".join([cmd_string, out, line.strip()])
        os.system(tmp) 
        #print(tmp)
