from django.urls import path
from feed.views import post_form, connections, groups

#URL Configuration
urlpatterns = [
    path('connections/', connections, name="connections"),
    path('groups/', groups, name="groups"),
    path('', post_form, name='feed'),
]