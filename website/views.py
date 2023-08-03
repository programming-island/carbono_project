from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def login(request):
    return render(request, 'cadastros/login.html',{})

def registrar(request):
    return render(request, 'cadastros/registrar.html',{})