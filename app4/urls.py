from django.conf.urls import url
from app4 import views

urlpatterns=[
    url(r'^users', views.users, name='users'),
    url(r'^$', views.index, name='index'),
]