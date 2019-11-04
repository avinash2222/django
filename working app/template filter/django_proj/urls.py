"""django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app6 import views

urlpatterns = [
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('app3/',include('app3.urls')),
    path('app4/',include('app4.urls')),
    path('app5/',include('app5.urls')),
    path('app6/',include('app6.urls')),
    path('admin/', admin.site.urls),
]
