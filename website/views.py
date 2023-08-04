from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        if not usuario or not senha:
            messages.error(request, 'Usuário/Senha não deve ser vazio')
            
    return render(request, 'cadastros/login.html',{})

def registrar(request):
    return render(request, 'cadastros/registrar.html',{})