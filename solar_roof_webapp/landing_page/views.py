from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landing_page/index.html', context=None, content_type=None, status=None, using=None)
