from django.urls import path
from .views import main

urlpatterns = [
    #if I get a url that has no / after it then run the main function
    path('', main)
]
