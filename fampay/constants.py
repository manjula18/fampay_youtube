SLEEP_TIME = 10
YOUTUBE_QUERY = 'cricket'
API_TIMEOUT = 30
SEARCH_URL = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&key={API_KEY}&type=video&q={YOUTUBE_QUERY}" \
             "&maxResults=50&order=date&publishedAfter={PUBLISHED_AFTER}&publishedBefore={PUBLISHED_BEFORE}"
API_KEY_INDEX = 0
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
MAX_LIMIT = 20
DEFAULT_LIMIT = 20
DEFAULT_OFFSET = 0
