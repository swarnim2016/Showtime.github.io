from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("movies",views.movies,name='movies'),
    path("register",views.register,name='register'),
    path("forest",views.forest,name='forest'),
    path("harry",views.harry,name='harry'),
    path("inception",views.inception,name='inception'),
    path("kgf",views.kgf,name='kgf'),
    path("doctor",views.doctor,name='doctor'),
    path("mission",views.mission,name='mission'),
    path("frozen",views.frozen,name='frozen'),
    path("shrek",views.shrek,name='shrek'),
    path("scooby",views.scooby,name='scooby')
  
]
