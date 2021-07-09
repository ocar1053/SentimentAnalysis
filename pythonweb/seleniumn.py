from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
f = open('test.txt', 'w', encoding="utf-8")
url = 'https://www.youtube.com/user/stanleyslol/videos'  # the board you want
driver.get(url)
seen = set()
for i in range(1000):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # for i in soup.find_all('a', class_="tgn9uw-3"):
    #     pos = i.text.find("輔")  # keyword you want find
    #     if pos >= 0:
    #         data = i.text + " " + "https://www.dcard.tw" + i.get('href')
    #         if data not in seen:
    #             driver.get("https://www.dcard.tw" +
    #                        i.get('href'))  # enter sub page
    #             soup = BeautifulSoup(driver.page_source, "html.parser")
    #             posttime = soup.find_all(
    #                 'div', class_="sc-1eorkjw-4 boQZzA")[1].text
    #             driver.back()  # 上一頁
    #             print(i.text, "https://www.dcard.tw" + i.get('href'), posttime)
    #             seen.add(data)
    time.sleep(0.1)
f.close()
