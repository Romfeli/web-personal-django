from django.shortcuts import render, HttpResponse

# Create your views here.

def home(requets):
    
    return render(requets, "core/home.html")

def about(requets):
    return render(requets, "core/about.html")



def contacto(requets):
    return render(requets,"core/contacto.html")