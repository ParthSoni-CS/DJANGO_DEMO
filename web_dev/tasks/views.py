from django.shortcuts import render,redirect
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority :", max_value=11, min_value=2)

tasks = ["clean your desk","learn webdev","go out for a walk","learn to speak french"]

def index(request):
    return render(request,"tasks/index.html",{'tasks':tasks})

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
            return redirect("home")
        else:
            return render(request,"tasks/add.html",{'form':form})

    return render(request,"tasks/add.html",{ 'form' : NewTaskForm()})

# Create your views here.
