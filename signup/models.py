from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


def validate_depaul_email(value):
    if not value.endswith('@depaul.edu'):
        raise ValidationError('Email must be a DePaul University email address (@depaul.edu)')

class Member(AbstractUser):
    class UserType(models.TextChoices):
        STUDENT = 'ST', 'Student'
        FACULTY = 'FA', 'Faculty'
        ALUMNI = 'AL', 'Alumni'

    username = None
    email = models.EmailField(unique=True, validators=[validate_depaul_email])
    user_type = models.CharField(max_length=2, choices=UserType.choices)
    title = models.CharField(max_length=255, blank=True, null=True)
    display_picture = models.ImageField(upload_to='member_display_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


# events
# groups
# post





