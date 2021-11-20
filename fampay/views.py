
from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.core import serializers
import json
from .models import YouTubeData
from .constants import DEFAULT_LIMIT, MAX_LIMIT, DEFAULT_OFFSET, DATETIME_FORMAT, INVALID_ORDER_BY
from .utility import to_dict


class FamPayData(View):
    def get(self, request, *args, **kwargs):
        """
        to get all the data from the db in pagenated form, search and sort on title and description fields are also supported by this api
        dy default the order_by value is -published_at, if any value is passed in orderby field then it will override the existing default value
        """
        get_params = request.GET

        try:
            limit = int(get_params.get('limit', DEFAULT_LIMIT))
            if limit > MAX_LIMIT:
                limit = DEFAULT_LIMIT
        except Exception:
            limit = DEFAULT_LIMIT
        try:
            offset = int(get_params.get('offset', DEFAULT_OFFSET))
        except Exception:
            offset = DEFAULT_OFFSET

        order_by = '-published_at'
        title = None
        description = None
        if 'title' in get_params:
            title = get_params['title']
        if 'description' in get_params:
            description = get_params['description']
        if 'order_by' in get_params:
            order_by = get_params.get('order_by', '')
            if not self.validate_order_by_key(order_by):
                return HttpResponse(content=json.dumps({'error': True, 'message': INVALID_ORDER_BY}),
                                    content_type='application/json', status=200)

        obj_list = self.get_objects(title, description)
        total = obj_list.count()
        new_offset = offset + limit

        obj_list = obj_list.order_by(order_by)[offset:new_offset]

        youtube_data = []
        for obj in obj_list:
            youtube_data.append(to_dict(obj, DATETIME_FORMAT))

        response = {'meta': {'total': total,
                             'next': new_offset,
                             'limit': limit,
                             'prev': offset-limit,
                             'offset': offset},
                    'objects': youtube_data}
        if total <= new_offset:
            response['meta']['next'] = None
        if offset == 0:
            response['meta']['prev'] = None
        return HttpResponse(content=json.dumps(response), content_type='application/json', status=200)

    @staticmethod
    def get_objects(title, description):
        """
        to fetch data form db based on the params
        """
        if title is None and description is None:
            obj_list = YouTubeData.objects.all()
        elif description is None:
            obj_list = YouTubeData.objects.filter(title__contains=title)
        elif title is None:
            obj_list = YouTubeData.objects.filter(description__contains=description)
        else:
            obj_list = YouTubeData.objects.filter(title__contains=title, description__contains=description)
        return obj_list

    @staticmethod
    def validate_order_by_key(order_by):
        """
        to validate order_by field, only 3 fields are allowed for sorting
        """
        for key in order_by.split(','):
            if key[0] == '-':
                key = key[1:]
            if key not in ['title', 'description', 'published_at']:
                return False
        return True
