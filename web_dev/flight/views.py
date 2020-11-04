from django.shortcuts import render
from .models import flight
def index(request):
    return render(request, "flight/index.html", {
        "flights": flight.objects.all()
    })
# Create your views here.
