from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('',views.inicio,name='inicio'),
    
]