from django.conf.urls import url
from django.contrib import admin
from Vramal.ramal.views import home, post_list

urlpatterns = [

    url(r'^$', (home)),
    
]