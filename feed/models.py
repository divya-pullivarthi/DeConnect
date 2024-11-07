from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from signup.models import Member

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField ()
    start_time = models.TimeField ()
    end_time = models.TimeField ()
    location = models.CharField(max_length=255)  
    
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    organizer = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='group_logos/', blank=True, null=True)
    description = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)  # For video uploads
    file = models.FileField(upload_to='post_files/', blank=True, null=True)      # For file uploads
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_announcement = models.BooleanField(default=False)  # To distinguish announcements
    emojis_used = models.TextField(blank=True)  # Store used emojis as a string

class Like(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

class CommentLike(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)

class Share(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')
    created_at = models.DateTimeField(auto_now_add=True)

