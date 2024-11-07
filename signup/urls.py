from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('', views.login_form),
    path('registration/', views.registration_form)
]