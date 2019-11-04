
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import HotelForm
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('app7/hotel_image_form.html') 
    else: 
        form = HotelForm() 
    return render(request, 'app7/hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded')