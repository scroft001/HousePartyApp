from django.urls import path
from .views import RoomView

urlpatterns = [
    #if I get a url that has no / after it then run the main function
    path('room/', RoomView.as_view())
]
