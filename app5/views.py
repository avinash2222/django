from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import FormModel


# Create your views here.
def index(request):
    return render(request, 'app5/index.html')

def form_name_view(request):
    form=FormModel()
    # ------to post data in kernal
    if request.method=="POST":
        form=FormModel(request.POST)

        if form.is_valid():
            form.save()
            print("Validation success!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    # --------end-----------

        

    return render(request, 'app5/form_page.html', {'form':form})
