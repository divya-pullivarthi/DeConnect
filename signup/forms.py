from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    #we used widget to hide the password using special characters like *.
    password = forms.CharField(
        widget = forms.PasswordInput(), min_length=8, max_length=20, label="Password" 
    )