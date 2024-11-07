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
        label='',
        min_length=8, 
        max_length=20
    )

# Registration Form
class RegistrationForm(forms.Form):
    first_name = forms.CharField(
                widget=forms.PasswordInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control fname'
        }),
        label='',
    )
    last_name = forms.CharField( widget=forms.PasswordInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control lname'
        }),
        label='',
    )
    email = forms.EmailField( widget=forms.PasswordInput(attrs={
            'placeholder': 'DePaul Email Address',
            'class': 'form-control'
        }),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }),
        label='',
        min_length=8,
        max_length=20
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }),
        label='',
        min_length=8,
        max_length=20
    )

    # Define choices for user type
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('alumni', 'Alumni'),
    ]

    # Add ChoiceField for user type
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        label="Are you a Student, Faculty, or Alumini?",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

     # Add checkbox for terms and conditions
    accept_terms = forms.BooleanField(
        required=True,
        label="I have read and agree to the Terms of Service and Privacy Policy. By creating an account, I understand and accept the following.",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'style': 'float: left; margin-right: 10px;'
        }),
    )
