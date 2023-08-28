from django.contrib import admin
from .models import Imovel,TipoImovel,FotosDosImoveis




# Register your models here.

admin.site.site_header = "Administração Carbono"
admin.site.index_title = "Administração do Site"
admin.site.site_title = "Site de administração do Carbono"

class FotosDosImoveisInline(admin.TabularInline):
    model = FotosDosImoveis
    extra = 1

class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'cidade')
    list_filter = ('cidade','preco')
    search_fields = ('titulo', 'descricao')
    inlines = [FotosDosImoveisInline]

admin.site.register(Imovel, ImovelAdmin)
admin.site.register(TipoImovel)


class TipoImovelAdmin(admin.ModelAdmin):
    pass

class FotosDosImoveisAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'foto')
