from django.urls import path
from.views import *
from myapp import views

urlpatterns = [
    
    path('',home),
    path("home/",home),
    path("registration/",registration),
    path("delete/<int:roll>",delete),
    path("edit/<int:roll>",views.edit),
    # path("doedit/<int:roll>",doedit),
   
]