from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/c/Mita0521/videos")
videoidlist = []
for i in range(1):
    scroll_height = 2000
    document_height_before = driver.execute_script(
        "return document.documentElement.scrollHeight")
    driver.execute_script(
        f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    atag = soup.findAll('a', href=True, id="video-title")
    for i in atag:
        videoid = i.get('href').split('v=')
        if (videoid[1]) not in videoidlist:
            videoidlist.append(videoid[1])
            print(videoid[1])
    document_height_after = driver.execute_script(
        "return document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break
print(videoidlist)
jsonString = json.dumps(videoidlist)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
