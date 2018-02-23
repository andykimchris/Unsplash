from django.shortcuts import render
from django.http import Http404

# Create your views here.


def index(request):

    title = 'Unsplash Images'
    context = {
        "title": title
    }
    return render(request, 'index.html', context)
