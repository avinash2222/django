from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from app7 import views
from django.conf.urls import url
  
urlpatterns = [ 
    url(r'^$', views.hotel_image_view, name = 'hotel_image_view'), 
    
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_DIR, 
                              document_root=settings.MEDIA_ROOT) 