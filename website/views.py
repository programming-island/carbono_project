from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from .models import Imovel,TipoImovel
from django.http import JsonResponse


# Create your views here.
def home(request):
    imoveis = Imovel.objects.filter(destaque=True)
    tipoimoveis = TipoImovel.objects.all()
    context = {'imoveis': imoveis, 'tipoimoveis':tipoimoveis}
    return render(request, 'home.html',context)

def imovel_pesquisa(request):
    return render(request, 'imoveis/pesquisa_imoveis.html')

@login_required
def graficos(request):
    imoveis = Imovel.objects.all() 
    context = {'imoveis': imoveis}
    return render(request, 'graficos.html', context)

def imovel_detalhes(request, imovel_id, imovel_nome):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    imovel.visualizacoes += 1
    imovel.save()

    context = {'imovel': imovel}
    return render(request, 'imoveis/detalhe_imovel.html', context)
    pass

def get_views_data(request):
    imoveis = Imovel.objects.all()
    data = {
        'labels': [imovel.titulo for imovel in imoveis],
        'data': [imovel.visualizacoes for imovel in imoveis],
    }
    return JsonResponse(data)

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

def LogoutView(request):
    logout(request)
    return redirect('/admin/')
        
