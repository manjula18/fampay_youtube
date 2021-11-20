import _thread, time
from .constants import SLEEP_TIME, YOUTUBE_QUERY, API_TIMEOUT, SEARCH_URL, DATETIME_FORMAT, API_KEY_INDEX
import requests
import datetime
from os import environ
API_KEYS = environ.get('API_KEYS', '').split(',')


def youtube_api_scheduler():
    _thread.start_new_thread(call_youtube_api, ())


def call_youtube_api():
    CURR_API_KEY_INDEX=API_KEY_INDEX
    url = SEARCH_URL
    published_after = datetime.datetime.utcnow() - datetime.timedelta(seconds=SLEEP_TIME)

    while True:
        next_page_token = None
        published_before = datetime.datetime.utcnow()
        while True:
            try:
                url = SEARCH_URL.format(YOUTUBE_QUERY=YOUTUBE_QUERY,
                                        API_KEY=API_KEYS[CURR_API_KEY_INDEX],
                                        PUBLISHED_AFTER=published_after.strftime(DATETIME_FORMAT),
                                        PUBLISHED_BEFORE=published_before.strftime(DATETIME_FORMAT))
                if next_page_token:
                    url += '&pageToken='+next_page_token

                response = requests.get(url=url, timeout=API_TIMEOUT)
            except Exception as e:
                print(e)
                continue
            if response.status_code == 200:
                youtube_data = response.json()
                next_page_token = youtube_data.get('nextPageToken', None)
                update_youtube_data_table(youtube_data)
            elif response.status_code == 429:
                print('data limit exhausted for the current API_KEY, so using another one')
                # use new api key
                CURR_API_KEY_INDEX += 1
                CURR_API_KEY_INDEX %= len(API_KEYS)
            if not next_page_token:
                break

        published_after = published_before
        print('data fetched from youtube, published before-', published_before.strftime(DATETIME_FORMAT))
        time.sleep(SLEEP_TIME)


def update_youtube_data_table(youtube_data):
    from .models import YouTubeData
    youtube_data_items = youtube_data.get('items', [])
    youtube_data_objects = []
    for item in youtube_data_items:
        snippet = item.get('snippet', {})
        if not snippet:
            continue
        thumbnail = snippet.get('thumbnails', {}).get('default', {}).get('url', '')
        if not thumbnail:
            for key, val in snippet.get('thumbnails', {}).items():
                thumbnail = val.get('url', '')
                if thumbnail:
                    break
        published_at = datetime.datetime.strptime(snippet.get('publishedAt', ''), '%Y-%m-%dT%H:%M:%SZ')
        youtube_data_objects.append(YouTubeData(title= snippet.get('title', ''),
                                                description= snippet.get('description', ''),
                                                published_at= published_at,
                                                url_thumbnail= thumbnail,
                                                channel_id= snippet.get('channelId', ''),
                                                channel_title=snippet.get('channelTitle', '')))
    if youtube_data_objects:
        result = YouTubeData.objects.bulk_create(youtube_data_objects)
        print(result, ' data inserted in youtube data table')
