from django.urls import path
from signup.views import CustomLoginView, registration_form, login_form

#URL Configuration
urlpatterns = [
    # path('', login_form),
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', registration_form)
]