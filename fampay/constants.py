# sleep time is used for thread sleep before calling youtube api
SLEEP_TIME = 30

# used for youtube query
YOUTUBE_QUERY = 'cricket'

#  timeout for api calls
API_TIMEOUT = 30

# Youtube search URL
SEARCH_URL = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&key={API_KEY}&type=video&q={YOUTUBE_QUERY}" \
             "&maxResults=50&order=date&publishedAfter={PUBLISHED_AFTER}&publishedBefore={PUBLISHED_BEFORE}"
API_KEY_INDEX = 0

#  this format is used in youtube request and response
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

# these are used for default values of limit and offset
MAX_LIMIT = 20
DEFAULT_LIMIT = 20
DEFAULT_OFFSET = 0

# error message for invalid order by field
INVALID_ORDER_BY = 'Invalid order by value in request params'
