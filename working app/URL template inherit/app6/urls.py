from  django.conf.urls import url
from app6 import views

app_name='app6'

urlpatterns=[
    url(r'', views.index, name='index'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]