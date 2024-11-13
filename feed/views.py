from django.shortcuts import render
from django.http import HttpResponse
from feed.feed import PostForm

# Create your views here.
def post_form(request):

    feepost_form = PostForm()

    return render(request, 'feed.html',{
        "post_form": post_form
    })


def connections(request):
    return render(request, 'connections.html')

