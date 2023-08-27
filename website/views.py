from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
import re
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .models import usuarios,Imovel


# Create your views here.
def home(request):
    imoveis = Imovel.objects.all()
    context = {'imoveis': imoveis}
    return render(request, 'home.html',context)

def imovel_detalhes(request,imovel_id):
    imovel = Imovel.objects.get(pk=imovel_id)
    return render(request, 'imoveis/detalhe_imovel.html',{'imovel':imovel})
    pass

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)


        if not usuario:
            senha_incorreta = False
            usuario_vazia = True
            return render(request, 'cadastros/login.html',{'usuario_vazia': True})
                
        elif not senha:
            senha_incorreta = False
            senha_vazia = True
            return render(request, 'cadastros/login.html',{'senha_vazia': True})

        if user is not None:
            login(request, user)
            senha_incorreta = False
            return redirect('/admin/')

        else:
            senha_incorreta = True
            return render(request, 'cadastros/login.html', {'senha_incorreta': True})
            
    return render(request, 'cadastros/login.html')
        
def logout_view(request):
    logout(request)
    return redirect('/admin/')
        
