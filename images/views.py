from django.shortcuts import render, redirect
from django.http import Http404
from .models import Gallery, Location, Category
# Create your views here.



def delete_image(request, id):

    image_id = Gallery.objects.get(id=id)

    if request.method == "POST":
        delete_image = image.get_delete_url()
        image.remove()
        return redirect(delete_image)

    context = {
        "image_id": image_id
    }
    return render(request, 'images.html', context)


def show_image_id(request, id):

    image_id = Gallery.objects.get(id=id)
    context = {
        "image_id": image_id
    }
    return render(request, 'images.html', context)


def search(request):

    images = Gallery.objects.all()
    query = request.GET.get('category')

    if query:
        newlist = images.filter(category__category__icontains=query)
     
        return render(request, 'search.html',{
            "newlist": newlist,
            "message": message,
        })

    else:
        message = "You haven't searched for any term"
        context = {
            "message": message
        }
        return render(request, 'search1.html', context)

def index(request):

    title = 'Unsplash Images'
    images = Gallery.my_images()

    context = {
        "title": title,
        "images": images
    }
    return render(request, 'index.html', context)
