from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'all-pics/index.html')


def search_results(request):

    return render(request, 'all-pics/index.hmtl')
