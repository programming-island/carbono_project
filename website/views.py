from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from .models import Imovel,TipoImovel,RedesSociais,Textosdofooter
from django.http import JsonResponse


# Create your views here.
def home(request):
    imoveis = Imovel.objects.filter(destaque=True)
    redessociais = RedesSociais.objects.all()
    tipoimoveis = TipoImovel.objects.all()
    mensagem = Textosdofooter.objects.all()
    
    search_query = request.GET.get('search')
    tipo_id = request.GET.get('tipo')
    
    filtro_tipoimovel = False
    filtro_tituloimovel = False
    tipo_imovel_psq = search_query
    
    if tipo_id:
        tipo_imovel = TipoImovel.objects.get(pk=tipo_id)
        tipo_imovel_nome = tipo_imovel.nome
        imoveis = imoveis.filter(tipo_imovel=tipo_imovel)
        filtro_tipoimovel = True
        tipo_imovel_psq = search_query
        
    else:
        tipo_imovel_nome = None
    
    if search_query:
        imoveis = Imovel.objects.filter(titulo__icontains = search_query)
        tipo_imovel_psq = search_query
        filtro_tituloimovel = True
        
    context = {'imoveis': imoveis, 
               'tipoimoveis':tipoimoveis,
               'redessociais':redessociais,
               'tipo_imovel_nome':tipo_imovel_nome,
               'tipo_imovel_psq':tipo_imovel_psq,
               'filtro_tipoimovel':filtro_tipoimovel,
               'filtro_tituloimovel':filtro_tituloimovel,
               'mensagems':mensagem,}
    
    if not imoveis:
        context['empty_message'] = "Nenhum imóvel encontrado para essa seleção."
        
    return render(request, 'home.html',context)

def quem_somos(request):
    mensagem = Textosdofooter.objects.all()
    return render(request, '_quem_somos.html', {'mensagems': mensagem})

def fale_conosco(request):
    mensagem = Textosdofooter.objects.all()
    return render(request, '_fale_conosco.html', {'mensagems': mensagem})

def  termos_condicoes(request):
    mensagem = Textosdofooter.objects.all()
    return render(request, '_termos_condicoes.html', {'mensagems': mensagem})

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
        
