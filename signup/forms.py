from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
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

    def clean_username(self):
        email = self.cleaned_data.get('username')
        return email.lower()  # Normalize email to lowercase


# Registration Form
class RegistrationForm(forms.ModelForm):
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

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'user_type', 'title', 'display_picture', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control fname'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control lname'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'DePaul Email Address',
                'class': 'form-control'
            }),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'display_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'user_type': 'Are you a Student, Faculty, or Alumni?',
            'title': '',
            'display_picture': '',
            'bio': '',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError('This field is required.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError('This field is required.')
        return last_name

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)  # Set the hashed password
        if commit:
            user.save()
        return user