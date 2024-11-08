from django.urls import path
from signup.views import CustomLoginView, registration_form, register_success
from django.contrib.auth.views import LogoutView

#URL Configuration
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='signup:login'), name='logout'),
    path('register/', registration_form, name='registration_form'),
    path('success/', register_success, name='register_success'),
]