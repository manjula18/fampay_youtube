from django.db import models


class YouTubeData(models.Model):

    title = models.TextField(db_index=True)

    description = models.TextField(db_index=True)

    published_at = models.DateTimeField(db_index=True)

    url_thumbnail = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    channel_id = models.TextField(default='')

    channel_title = models.TextField(default='')

