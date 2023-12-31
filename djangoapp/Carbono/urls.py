from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('imovel/<int:imovel_id>_<slug:imovel_nome>/', views.imovel_detalhes, name = 'imovel_detail'),
    path('grafico/', views.graficos, name='graficos'),
    path('api/views_data/', views.get_views_data, name='get_views_data'),
    path('quem-somos/', views.quem_somos, name='_quem_somos'),
    path('fale-conosco/', views.termos_condicoes, name='_fale_conosco'),
    path('termos-condicoes/', views.termos_condicoes, name='_termos_condicoes'),
    path('imovel/pesquisa/', views.imovel_pesquisa, name = 'imovel_pesquisa'),
]
