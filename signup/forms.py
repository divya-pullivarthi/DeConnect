from django import forms

# Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control'
        }),
        label=''
       )
#we used widget to hide the password using special characters like *.
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }),
        label=''
    # password = forms.CharField(
    #     widget = forms.PasswordInput(), min_length=8, max_length=20, label="Password" 
    )
