from django.shortcuts import render, redirect
from django.http import Http404
from .models import Gallery, Location, Category
# Create your views here.


def index(request):

    title = 'Unsplash Images'
    images = Gallery.my_images()

    context = {
        "title": title,
        "images": images
    }
    return render(request, 'index.html', context)


def show_image_id(request, id):

    image_id = Gallery.objects.get(id=id)
    context = {
        "image_id": image_id
    }
    return render(request, 'images.html', context)


def search_results(request):

    if 'category' in request.GET and request.GET['q']:
        search_term = request.GET.get('category')
        category = Category.search_by_category(search_term)
        message = f"{search_term}"
        images = Gallery.my_images()

        context = {
            "category": category,
            "message": message,
            "images": images

        }
        return render(request, 'search.html', context)

    else:
        message = "You haven't searched for any term"

        context = {
            "message": message
        }
        return render(request, 'search.html', context)
