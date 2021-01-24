import os 
import sys

single_dl = 'C:\ outube-dl\youtube-dl.exe --ignore-errors --format best --output ' 
pl_dl = 'C:\youtube-dl\youtube-dl.exe --ignore-errors -f best --output "%(title)s.%(ext)s" --yes-playlist '

#open the text file required
file = open(sys.argv[1])
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
