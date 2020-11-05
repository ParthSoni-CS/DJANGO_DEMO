from django.shortcuts import render
from .models import flight

# Create your views here.
def index(request):
    return render(request, "flight/index.html", {
        "flights": flight.objects.all()
    })

def flight_det(request,flight_id):
    flight_details = flight.objects.get(pk = flight_id)
    return render(request, "flight/flight_det.html",{
        "flight_det":flight_details
    })
