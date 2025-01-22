# Task 1 

import urllib.request
import json
import csv
import time 

# URLs
# https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1
# https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2

with urllib.request.urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2') as mrt_file:
    mrt_origin_data  = mrt_file.read().decode("utf-8")
    mrt_data  = [ mrt for mrt in json.loads(mrt_origin_data)["data"]]
mrt_list = []
for station in mrt_data:
    address = station["address"][5:8]
    temp_dic = [station["SERIAL_NO"],station["MRT"],address]
    mrt_list.append(temp_dic)

# spot.csv , mrt.csv
with urllib.request.urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1') as f1:
    original_spot_data = f1.read().decode('utf-8')
    spot_data = json.loads(original_spot_data)["data"]["results"]
individal_spot_data = []
mrt_attractions = {station[1]:[] for station in mrt_list}

for spot in spot_data:
    imageURl = ""
    temp = spot["filelist"].split("http")
    imageURl = "http"+temp[1]
    for data in mrt_list:
        if data[0] == spot['SERIAL_NO']:
            district = data[2]
            mrt_attractions[data[1]].append(spot['stitle'])
            break

    individal_spot_data.append([spot['stitle'], district,spot['longitude'],spot['latitude'],imageURl])

mrt_result = []
for mrt,attractions in mrt_attractions.items():
    temp = [mrt]
    for attraction in attractions:
        temp.append(attraction) 
    mrt_result.append(temp)


with open ("spot.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(individal_spot_data)

with open ("mrt.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(mrt_result)



# Task2
# URL :https://www.ptt.cc/bbs/Lottery/index.html

from bs4 import BeautifulSoup
from datetime import datetime

headers = {"cookie":"over18=1",'user-agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"}
page_link = ["https://www.ptt.cc/bbs/Lottery/index.html"]
post_data = []
article = []
for i in range(3):

    req = urllib.request.Request(page_link[i],headers = headers ) 
    data = urllib.request.urlopen(req)

    root = BeautifulSoup(data,"html.parser")
    
    page = root.find("a",string = "‹ 上頁")
    page_link.append("https://www.ptt.cc" + page['href'])

    posts = root.find_all("div",class_= "r-ent")
    for post in posts:
        if  post.find("div",class_= "title").a is not None :
            title = post.find("div",class_= "title").get_text().strip("\n")
            url = "https://www.ptt.cc" + post.find("div",class_="title").a.get("href")
            count = post.find("div",class_="nrec").span
            if count is  None:
                count = "0"
            elif int(count.get_text()) < 0:
                count = "-1"
            else:
                count = count.get_text()
            post_data.append([title,count,url])
        else:
            pass

for post in post_data:
    try:
        post_req = urllib.request.Request(post[-1], headers = headers )
        post_data = urllib.request.urlopen(post_req)
        post_content = BeautifulSoup(post_data,"html.parser")
        time_data = post_content.find_all("span",class_="article-meta-value")
        if time_data :
            post_time= time_data[-1].get_text()
        else:
            post_time = ""
    except urllib.error.HTTPError as e:        
        print({e.code},post[-1])
        post_time = f"Error:{e.code}/{e.reason}"
    article.append([post[0],post[1],post_time])


with open("article.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(article)

