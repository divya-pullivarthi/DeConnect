from django.db import models
from django.core.exceptions import ValidationError


def validate_depaul_email(value):
    if not value.endswith('@depaul.edu'):
        raise ValidationError('Email must be a DePaul University email address (@depaul.edu)')   
    
# Create your models here.
class Members (models.Model):
    class UserType(models.TextChoices):
        STUDENT = 'ST', 'Student'
        FACULTY = 'FA', 'Faculty'
        ALUMNI = 'AL', 'Alumni'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(validators=[validate_depaul_email])
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=2,choices=UserType.choices)
    title = models.CharField(max_length=255)
    display_picture = models.ImageField(upload_to='member_display_photos/', blank=True, null=True)
    bio = models.TextField()

# events
# groups
# post





