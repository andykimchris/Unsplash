from django.http import Http404
from django.shortcuts import redirect, render

from .models import Category, Gallery, Location

# Create your views here.


def delete_image(request, id):

    image_id = Gallery.objects.get(id=id)

    if request.method == "POST":
        delete_image = image.get_delete_url()
        image.remove()
        return redirect(delete_image)

    return render(request, 'images.html', {
        "image_id": image_id
    })


def show_image_id(request, id):

    image_id = Gallery.objects.get(id=id)

    return render(request, 'images.html', {
        "image_id": image_id
    })


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Gallery.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {
            "message": message,
            "category": searched_images
        })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def search_location(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_images = Gallery.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'search1.html', {
            "message": message,
            "location": searched_images
        })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search1.html', {"message": message})


def index(request): 

    title = 'Unsplash Images'
    images = Gallery.objects.all()

    return render(request, 'index.html', {
        "title": title,
        "images": images
    })
