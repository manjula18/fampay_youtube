from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.core import serializers
import json
from .models import YouTubeData
from .constants import DEFAULT_LIMIT, MAX_LIMIT, DEFAULT_OFFSET


class FamPayData(View):
    def get(self, request, *args, **kwargs):
        try:
            limit = int(request.GET.get('limit', DEFAULT_LIMIT))
            if limit > MAX_LIMIT:
                limit = DEFAULT_LIMIT
        except Exception:
            limit = DEFAULT_LIMIT
        try:
            offset = int(request.GET.get('offset', DEFAULT_OFFSET))
        except Exception:
            offset = DEFAULT_OFFSET

        obj_list = YouTubeData.objects.order_by('-published_at')[offset:offset+limit]
        new_offset = offset+limit+1
        # serialize queryset
        serialized_queryset = serializers.serialize('json', obj_list)
        return HttpResponse(serialized_queryset, content_type='application/json')

        # return HttpResponse(content=json.dumps(message), content_type='application/json', status=401)


def search(request):
    title = request.GET.get('title', '')
    description = request.GET.get('description', '')

    if title and description:
        obj_list = YouTubeData.objects.filter(title__contains=title, description__contains=description).order_by('-published_at')
    elif title:
        obj_list = YouTubeData.objects.filter(title__contains=title).order_by('-published_at')
    else:
        obj_list = YouTubeData.objects.filter(description__contains=description).order_by('-published_at')
    serialized_queryset = serializers.serialize('json', obj_list)
    return HttpResponse(serialized_queryset, content_type='application/json')