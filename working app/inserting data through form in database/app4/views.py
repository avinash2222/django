from django.shortcuts import render

# Create your views here.
# from app4.models import User
from app4.forms import NewUserForm

def index(request):
    return render(request, 'app4/index.html')

def users(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form INVALID')

    return render(request, 'app4/users.html',{'form':form})

