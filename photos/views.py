from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.

def index(request):
    
    images = Image.all_images()
    return render(request, 'all-pics/index.html', {"images":images})


def search_results(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search_results.html',{"message":message,"images": searched_images,'categories': categories,
                       "locations": locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search_results.html',{"message":message})