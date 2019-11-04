from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text': 'hello world', 'number':100}
    return render(request, 'app6/index.html', context_dict)

def base(request):
    return render(request, 'app6/base.html')

def other(request):
    return render(request, 'app6/other.html')

def relative(request):
    return render(request, 'app6/relative_url_templates.html')
