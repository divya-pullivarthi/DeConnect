from django.urls import path
from signup.views import CustomLoginView, registration_form, register_success

#URL Configuration
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', registration_form, name='registration_form'),
    path('success/', register_success, name='register_success'),
]