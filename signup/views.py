from django.shortcuts import render
from django.http import HttpResponse
from signup.forms import LoginForm
from signup.forms import RegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.
def login_form(request):

    login_form = LoginForm()

    return render(request, 'login.html',{
        "login_form": login_form
    })

def registration_form(request):

    registration_form = RegistrationForm()

    return render(request, 'registration.html',{
        "registration_form": registration_form
    })


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'