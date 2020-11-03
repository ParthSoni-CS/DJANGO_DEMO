from django.shortcuts import render

tasks = ["clean your desk","learn webdev","go out for a walk","learn to speak french"]

def index(request):
    return render(request,"tasks/index.html",{'tasks':tasks})

# Create your views here.
