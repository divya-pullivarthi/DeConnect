from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('feed/', views.post_form)
]