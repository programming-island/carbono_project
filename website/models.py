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