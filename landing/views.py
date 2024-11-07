import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Event

@login_required
def landing_page(request):
    # Fetch recent posts
    recent_posts = Post.objects.order_by('-created_at')[:5]  # Get 5 most recent posts
    
    # Fetch upcoming events
    upcoming_events = Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date')[:3]  # Get 3 upcoming events
    
    context = {
        'user': request.user,
        'recent_posts': recent_posts,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'landing.html', context)