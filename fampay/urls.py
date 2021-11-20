from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('youtube_data', csrf_exempt(views.FamPayData.as_view()), name='get_data'),
]