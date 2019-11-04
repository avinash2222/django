from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app6/index.html')

def other(request):
    return render(request, 'app6/other.html')

def relative(request):
    return render(request, 'app6/relative_url_templates.html')
