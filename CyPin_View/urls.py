from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', index_view),
    url(r'^login', login_view),
    url(r'^home_head$', home_head),
]