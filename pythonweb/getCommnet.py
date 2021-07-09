from googleapiclient.discovery import build
import json
f = open('data.json',)
data = json.load(f)
api_key = 'youkey'
replies = []


def video_comments(video_id):
    # empty list for storing reply

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey='youkey')
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


# Call function
for i in data:
    try:
        video_comments(i)
    except:
        continue
print(len(replies))
with open('commnet.json', 'w', encoding='utf-8') as f:
    json.dump(replies, f, ensure_ascii=False, indent=4)
