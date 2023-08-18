from django.contrib import admin
from .models import Imovel,TipoImovel
from django.contrib.admin import AdminSite



# Register your models here.

admin.site.site_header = "Administração Carbono"
admin.site.index_title = "Administração do Site"
admin.site.site_title = "Site de administração do Carbono"


admin.site.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'cidade')
    list_filter = ('cidade',)
    search_fields = ('titulo', 'descricao')

admin.site.register(TipoImovel)
class TipoImovelAdmin(admin.ModelAdmin):
    pass

