from django.db import models
from django.utils import timezone
import re
import os

# Create your models here.

class TipoImovel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Imóvel'
        verbose_name_plural = 'Tipos de Imóveis'
        ordering = ['nome']

class Imovel(models.Model):
    titulo = models.CharField(verbose_name="Título do Imóvel",max_length=200)
    tipo_imovel = models.ForeignKey(TipoImovel,verbose_name="Tipo do Imóvel", on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(verbose_name="Preço do Imóvel",max_digits=15, decimal_places=2)
    endereco = models.CharField(verbose_name="Endereço",max_length=200)
    cidade = models.CharField(verbose_name="Cidade",max_length=100)
    qtd_quartos = models.IntegerField(verbose_name="Qtd Quartos")
    qtd_banheiros = models.IntegerField(verbose_name="Qtd Banheiros")
    qtd_comodos = models.IntegerField(verbose_name="Qtd Comodos Totais")
    data_geracao = models.DateTimeField(default=timezone.now, editable=False)
    destaque = models.BooleanField(default=False)
    visualizacoes = models.PositiveIntegerField(default=0,editable=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['titulo']

def upload_to(instance,filename): 
    base_filename, extension = os.path.splitext(filename)
    title = instance.imovel.titulo
    # Remove caracteres especiais e espaços
    clean_title = re.sub(r'[^\w\s-]', '', title).strip()
    # Substitui espaços por underscores
    clean_title = re.sub(r'\s+', '_', clean_title)
    # Limita o tamanho do título para evitar nomes de arquivo muito longos
    max_length = 30  
    final_title = clean_title[:max_length]
    return f"imoveis/{final_title}-{instance.imovel.id}{extension}"
    
class FotosDosImoveis(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    foto =  models.ImageField(upload_to=upload_to)

    def __str__(self):
        return f"Foto do imóvel: {self.imovel.titulo}"

    class Meta:
        verbose_name = 'Foto do Imóvel'
        verbose_name_plural = 'Fotos dos Imóveis'
        
 
class RedesSociaisManager(models.Manager):
    def get_singleton(self):
        obj, created = self.get_or_create(pk=1)
        return obj       
        
class RedesSociais(models.Model):
    facebook = models.CharField(verbose_name='Facebook',max_length=300)
    instagram = models.CharField(verbose_name='Instagram',max_length=300)
    whatsapp = models.CharField(verbose_name='WhatsApp',max_length=300)
    
    
    def save(self, *args, **kwargs):
        if not self.pk and RedesSociais.objects.exists():
            return  # Apenas uma instância permitida
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Socias'
        
    
    def __str__(self):
        return "Configurações de Redes Sociais"