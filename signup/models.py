from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class MemberManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)


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

    objects = MemberManager()

    def __str__(self):
        return self.email


# events
# groups
# post





