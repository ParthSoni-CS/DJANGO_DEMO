from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("<int:flight_id>",views.flight_det,name="flight_det"),
]

