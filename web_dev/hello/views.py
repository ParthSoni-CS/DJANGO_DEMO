from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Helloooo anonyms!")

def greet(request,name):
    return render(request, 'hello\index.html', {'name' : name})

