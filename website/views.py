from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        
        if not usuario or not senha:
            messages.error(request, 'Usuário/Senha não deve ser vazio')
            
        user = authenticate(request, username=usuario, password=senha)
        if  user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha invalido, verifique!')
            return render(request,'cadastros/login.html')

    return render(request, 'cadastros/login.html', {})
        
def logout_view(request):
    logout(request)
    return redirect('home')
        
def registrar(request):
    return render(request, 'cadastros/registrar.html',{})