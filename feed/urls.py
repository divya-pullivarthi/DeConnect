from django.urls import path
from feed.views import post_form, connections, groups, events

#URL Configuration
urlpatterns = [
    path('connections/', connections, name="connections"),
    path('groups/', groups, name="groups"),
    path('events/', events, name="events"),
    path('', post_form, name='feed'),
]