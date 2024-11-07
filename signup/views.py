from django.shortcuts import redirect, render
from django.http import HttpResponse
from signup.forms import LoginForm
from signup.forms import RegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signup:register_success')  # Replace with your success URL
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": form
    })

def register_success(request):
    return render(request, 'register_success.html')