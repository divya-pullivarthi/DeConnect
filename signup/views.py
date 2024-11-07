from django.shortcuts import render
from django.http import HttpResponse
from signup.forms import LoginForm

# Create your views here.
def say_hello(request):

    login_form = LoginForm()

    return render(request, 'login.html',{
        "login_form": login_form
    })