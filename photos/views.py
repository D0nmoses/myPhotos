from django.shortcuts import render

# Create your views here.

def index(request):
    
    images = Image.all_images()
    return render(request, 'all-pics/index.html', {"images":images})


def search_results(request):

    return render(request, 'all-pics/index.hmtl')
