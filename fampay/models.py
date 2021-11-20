from django.db import models


class YouTubeData(models.Model):

    # title of youtube video
    title = models.TextField(db_index=True)

    #  description og youtube video
    description = models.TextField(db_index=True)

    # video published timestamp
    published_at = models.DateTimeField(db_index=True)

    # url of the video
    url_thumbnail = models.TextField()

    # created at timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # channel id of youtube uploader
    channel_id = models.TextField(default='')

    # channel name of youtube uploader
    channel_title = models.TextField(default='')

