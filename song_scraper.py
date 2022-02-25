import pickle
import regex as re

import requests
from bs4 import BeautifulSoup as bs
import time
import warnings
warnings.filterwarnings("ignore")

baseURL="https://telugulyrics.com/lyricist/sirivennela-seetharama-sastry/page/"
songURLs=[]
for i in range(1,47):
    temp_url=baseURL+str(i)
    print(temp_url)
    html=requests.get(temp_url,verify=False).text
    mainSoup=bs(html,"html.parser")
    try:
        for i in mainSoup.find_all("div",{"class":re.compile("list-line")}):
            try:
                link=i.find("a")["href"]
                print(link)
                songURLs.append(link)
            except:
                print("Link not found")
    except:
        print("Song list not found")
    # Manners
    time.sleep(2.5)

print("Collected "+str(len(songURLs))+" song URL")
pickle.dump(songURLs,open("songs_url.txt","wb"))
