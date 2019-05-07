from django.urls import include, path 
from django.contrib import admin
from . import views

urlpatterns = [ path('home/', views.home, name='home'),
                path('index/', views.index, name='index'),

]
