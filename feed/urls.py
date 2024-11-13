from django.urls import path
from feed.views import post_form, connections

#URL Configuration
urlpatterns = [
    path('connections/', connections, name="connections"),
    path('', post_form, name='feed'),
]