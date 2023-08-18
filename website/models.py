from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class usuarios(models.Model):
    iduser = models.ForeignKey(User , on_delete=models.CASCADE)
    nome = models.CharField(max_length=50,blank=True)
    sobrenome = models.CharField(max_length=100,blank=True)
    cpf = models.CharField(max_length=14, blank= True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField(max_length=8)
    data_criacao = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length = 1)
    cep = models.IntegerField(default=0)
    inativo = models.BooleanField(default=False)

class TipoImovel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    titulo = models.CharField(verbose_name="Título do Imóvel",max_length=200)
    tipo_imovel = models.ForeignKey(TipoImovel,verbose_name="Tipo do Imóvel", on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(verbose_name="Preço do Imóvel",max_digits=5, decimal_places=2)
    endereco = models.CharField(verbose_name="Endereço",max_length=200)
    cidade = models.CharField(verbose_name="Cidade",max_length=100)
    qtd_quartos = models.IntegerField(verbose_name="Qtd Quartos")
    qtd_banheiros = models.IntegerField(verbose_name="Qtd Banheiros")
    qtd_comodos = models.IntegerField(verbose_name="Qtd Comodos Totais")
    foto = models.ImageField(verbose_name="Foto do Imóvel", upload_to="imoveis/", default="imoveis/default.png")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
