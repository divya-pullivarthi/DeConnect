from django.urls import path
from feed.views import post_form, connections

#URL Configuration
urlpatterns = [
    path('', post_form),
    path('connections/', connections),
]