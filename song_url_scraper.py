import re
import warnings
import requests
from bs4 import BeautifulSoup as bs
import time,os,pickle
warnings.filterwarnings("ignore")

def filterHTML(string:str)->str:
    start=string.find("</h3>")
    answer=string[start+5:]
    end=answer.find("<div>")
    answer=answer[:end]
    answer=answer.replace("<br/>","\n")
    return answer.strip()

#loading pickle song url object
song_url=pickle.load(open("songs_url.txt","rb"))

dirName="corpus"
fileName=dirName+"/song"
currIter=1
try:
    os.mkdir(dirName)
except FileExistsError:
    print("INFO: corpus dir creation not needed")


for i in song_url:
    html=requests.get(i,verify=False).text
    soup=bs(html,"html.parser")
    main_text=soup.find("div",{"class":re.compile("lyric-text")})
    check=soup.find("h3",{"class":"translated"})
    if check is None:
        pass
    with open(fileName+str(currIter)+".txt","w") as f:
        f.write(filterHTML(str(main_text)))
        currIter+=1
    time.sleep(2)
print("created "+str(currIter)+" songs")