import os 

cmd_string = "C:\youtube-dl\youtube-dl.exe --ignore-errors --format best"
#open the text file required
file = open("urls.txt")
Lines = file.readlines() 

for line in Lines: 
    tmp = " ".join([cmd_string, line.strip()])
    os.system(tmp) 
