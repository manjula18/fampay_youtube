<div align="center">

  <h3 align="center">FamPay YouTube Assignment</h3>

</div>


## About The Project

We need an API to fetch latest videos from YouTube sorted in reverse chronological order of their published date-time from YouTube for a given tag/search query in a paginated response.

### Basic Requirements:

#### Project brief
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimised.

#### Implementation details
In the project I have created an API to get all the data stored in YouTube data table in a paginated format, where offset and limit can be passed and search functionality on title and description. This does not only search with exact match but also checks if the parameter value is present in title or description.

In parallel one thread is created while starting the server which calls the YouTube API, fetches the data and inserts it into youtube_data table. I have added 2 keys in the environment variables which switches when the api limit is exhausted. I am using local sqlite3 db for storing the data.

I have stored all the constant values in a file and using 30 seconds for api sleep time and cricket as the youtube query. Also created a utility library for common methods.

### Built With


* Python3
* Django

## Getting Started

I have used docker to build the project, which internally install python3, git and run the server
### Prerequisites

* Docker

    Switch to the project folder and execute the below commands to run the docker
  ```sh
  docker-compose build --no-cache #for building the server
  docker-compose up #for running the built server
  docker-compose up --build #restart the server
  ```

### Installation

Below is the step to run the code locally without docker
1. Create an app in google console and enable YouTube api v3 and create api key to access the api, store this api key in an environment variables(API_KEYS) with comma separated for multiple keys
2. Clone the repo
   ```sh
   git clone https://github.com/manjula18/fampay_youtube.git
   ```
3. Create an environment variable and activate it
   ```sh
   virtualenv venv
   source venv/bin/activate
   ```
4. Install all the required libraries present in "requirements.txt"
   ```js
   pip3 install -r requirements.text
   ```
5. Run the commands for makemigrations and migrate then start the server
   ```js
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver 0.0.0.0:8000
   
   ```



## API 

Endpoint: http://localhost:8000/fampay/youtube_data?limit=5&offset=0&title=cricket&description=cricket&order_by=-published_at

Method: GET

Response:

```js
   {
    "meta": {
        "total": 112,
        "next": 5,
        "limit": 5,
        "prev": null,
        "offset": 0
    },
    "objects": [
        {
            "id": 113,
            "title": "cricket KBC, can anyone answer 🤔 || cricket tiktok video, new cricket tiktok #shorts",
            "description": "",
            "published_at": "2021-11-20T11:24:59Z",
            "url_thumbnail": "https://i.ytimg.com/vi/N7UMHJZh_UQ/default.jpg",
            "created_at": "2021-11-20T11:25:11Z",
            "channel_id": "UCD4umox5sup3GPgLW6GzbSA",
            "channel_title": "👲 MRD Daily Short 👲"
        },
        {
            "id": 112,
            "title": "Akash chopra on roller throw #ytshorts #shorts #cricket",
            "description": "",
            "published_at": "2021-11-20T11:23:42Z",
            "url_thumbnail": "https://i.ytimg.com/vi/6VyK66nOea4/default.jpg",
            "created_at": "2021-11-20T11:23:51Z",
            "channel_id": "UCDkSNsTNQ2trdpOVMmyyk1A",
            "channel_title": "Akashvani cricket vids"
        },
        {
            "id": 111,
            "title": "Dinesh Kartik last ball six in Nidhas Trophy #cricket #shorts #dineshkarthik",
            "description": "rohit sharma whatsapp status tamil, rohit sharma whatsapp status full screen, rohit sharma whatsapp status telugu, rohit sharma whatsapp status malayalam, ...",
            "published_at": "2021-11-20T11:21:12Z",
            "url_thumbnail": "https://i.ytimg.com/vi/Y4SrLJXCnoc/default.jpg",
            "created_at": "2021-11-20T11:21:26Z",
            "channel_id": "UCDbsIFT0EHGOhk6bbOl7wEA",
            "channel_title": "Cricket Shorts "
        },
        {
            "id": 110,
            "title": "Most handsome pakistani cricketers in White uniforms |Pakistan cricket team photos| pakistan players",
            "description": "Pakistani cricket match photos in White Uniforms Pakistan cricket team photos most handsome pakistani cricketers Most beautiful pakistani cricketer beautiful ...",
            "published_at": "2021-11-20T11:19:25Z",
            "url_thumbnail": "https://i.ytimg.com/vi/dfGIVDV9oJQ/default_live.jpg",
            "created_at": "2021-11-20T11:19:33Z",
            "channel_id": "UCge8hq7rctCwkEG6boQAF2Q",
            "channel_title": "Motivational Gateway"
        },
        {
            "id": 109,
            "title": "wow🤔 cricket amazing shot 💯👌👌",
            "description": "",
            "published_at": "2021-11-20T11:18:24Z",
            "url_thumbnail": "https://i.ytimg.com/vi/8YWls607jJg/default.jpg",
            "created_at": "2021-11-20T11:18:36Z",
            "channel_id": "UCZIFkSpUWCmDHxdyAgcmWEA",
            "channel_title": "chejara zone"
        }
    ]
}
   
   ```



## Roadmap

- Add Cronjob in place of threading for calling YouTube search api 
- Add dashboard to view and interact with the data built on top of the API
- Optimize search api, so that it can search videos containing partial match: For this either we can search in the db with splitting the filter value and then searching in the db with and parameter, or we can store reverse indexes in another table with id associated with this and ony respond with the ids which are common.
- Use an online db to store the data

## Contact

Manjula Choudhary - manjulachoudhary18@gmail.com

Project Link: https://github.com/manjula18/fampay_youtube

