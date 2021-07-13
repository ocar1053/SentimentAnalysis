from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import asyncio
from googleapiclient.discovery import build
driver = webdriver.Chrome()
api_key = 'yourapi'
driver.get("https://www.youtube.com/c/%E9%BB%83%E6%B0%8F%E5%85%84%E5%BC%9F/videos")
videoidlist = []
replies = []
youtuberName = "yellowboy"


def getVideoid():
    for i in range(2):
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
    driver.close()


def video_comments(video_id):
    # empty list for storing reply

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey='yourapi')
    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id).execute()

    # iterate video response
    while video_response:
        # extracting required info
        # from each result object
        for item in video_response['items']:
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            print(comment)
            if comment not in replies:
                replies.append(comment)
            # empty reply list
        else:
            break


def main():
    getVideoid()
    for i in videoidlist:
        try:
            video_comments(i)
        except:
            continue
    print(len(replies))
    with open('comments/dailyLive/'+youtuberName + '.json', 'w', encoding='utf-8') as f:
        json.dump(replies, f, ensure_ascii=False, indent=4)


main()


# jsonString = json.dumps(videoidlist)
# jsonFile = open("data.json", "w")
# jsonFile.write(jsonString)
