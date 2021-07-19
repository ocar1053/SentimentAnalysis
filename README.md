<br />
<p align="center">

  <h3 align="center">中文情感分析分析YouTube評論之工具</h3>

  <p align="center">
        利用中文情感分析得出評論分數
    <br />
    <a href="https://github.com/ocar1053/SentimentAnalysis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ocar1053/SentimentAnalysis/issues">Report Bug</a>
    ·
    <a href="https://github.com/ocar1053/SentimentAnalysis/pulls">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>目錄</summary>
  <ol>
    <li>
      關於專案</a>
      <ul>
        <li>使用工具與資料</a></li>
      </ul>
    </li>
    </li>
    <li>功能展示</a></li>
    <li>所需套件下載</a></li>
    <li>使用技術</a></li>
    <li>聯絡資料</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## 關於專案

此專案是個夠大量獲取 youtube 評論並對其進行情感分析的工具，可以對結果進行數據分析，亦或是套用其他模型進行語言處理。

作法為使用 python 爬蟲套件與 youtube api 獲取大量 youtube 評論，將檔案儲存回 json 檔後，使用 python 對此檔案中的大量留言進行情感分析

#### 使用工具與資料

-   [Python](https://www.python.org/)
-   [YouTube Data API](https://developers.google.com/youtube/v3)
-   [selenium](https://pypi.org/project/selenium/)

<!-- GETTING STARTED -->

## 功能展示

輸入 api 和 youtube 頻道主總影片網址(ex: https://www.youtube.com/c/%E9%BB%83%E6%B0%8F%E5%85%84%E5%BC%9F/videos )，對一到兩頁(可自由增加)的影片評論進行爬取。

```python
api_key = 'youapi'
driver.get("頻道主總影片網址")
```

<br>

打開儲存的評論 json 檔後，對大量評論進行情感分析，分數為 0 到 1 之間，越接近 1 代表越高機率為正向評論。

```python
f = open('comments/dailyLive/'+youtuberName + '.json', encoding='utf-8')
dataComment = json.load(f)
f.close()
```

![Product Name Screen Shot][product-screenshot]

## 所需套件下載

-   [selenium](https://pypi.org/project/selenium/)
-   [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
-   [snownlp](https://pypi.org/project/snownlp/)

## 使用技術

-   自然語言處理
-   串接 YouTube Data API
-   Python 爬蟲

## 聯絡資料

謝頤賢 - [謝頤賢臉書](https://www.facebook.com/profile.php?id=100002653454736) - ocar8951@gmail.com

Github Link: [https://github.com/ocar1053](https://github.com/ocar1053)

[product-screenshot]: images/anaysize.png
[search-screenshot]: images/getcomment.png
