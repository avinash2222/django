from  django.conf.urls import url
from app6 import views

app_name='app6'

urlpatterns=[
    url('other/', views.other, name='other'),
    #url(r'^relative/$', views.relative, name='relative'),
    url('', views.index, name='index'),
]