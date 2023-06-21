from django.shortcuts import render
from .models import Contact

def home(request):
    if request.method=="POST":
        contact = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name = name

    return render(request, 'index.html')