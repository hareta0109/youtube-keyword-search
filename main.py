import sys
import json
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

MAX_RESULTS = 50
DEVELOPER_KEY = 'REPLACE_ME' # replace here
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def youtube_video_search(keyword):
    search_response = youtube.search().list(
        q = keyword,
        type = 'video',
        part = 'id,snippet',
        maxResults = MAX_RESULTS
    ).execute()
    return search_response['items']

def youtube_video_statictics(video_id):
    statistics_response = youtube.videos().list(
        part = 'statistics',
        id = video_id
    ).execute()
    if len(statistics_response['items']):
        return statistics_response['items'][0]['statistics']
    else:
        return None

def search(keyword):
    video_list = youtube_video_search(keyword)
    df_video_raw = pd.DataFrame(video_list)
    df_video_id = pd.DataFrame(list(df_video_raw['id']))['videoId']
    df_video_data = pd.DataFrame(list(df_video_raw['snippet']))[['channelTitle','publishedAt','channelId','title','description']]
    df_video = pd.concat([df_video_id, df_video_data], axis=1)
    df_video_static = pd.DataFrame(list(df_video['videoId'].apply(lambda id : youtube_video_statictics(id))))[['viewCount','likeCount']]
    df_result = pd.concat([df_video, df_video_static], axis=1)
    js_result = json.dumps(json.loads(df_result.to_json(orient='records')), indent=4)
    return js_result

if __name__ == '__main__':
    parser = sys.argv
    if(len(parser)!=2):
        print('One Argument of search keyword is needed.')
        exit()
    keyword = parser[1]

    try:
        result = search(keyword)
        print(result)
    except HttpError as e:
        print('HTTP error %d occurred:\n%s' % (e.resp.status, e.content))