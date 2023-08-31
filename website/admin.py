from django.contrib import admin
from .models import Imovel,TipoImovel,FotosDosImoveis,RedesSociais,Textosdofooter

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

admin.site.register(Textosdofooter)
class TextosFooterAdmin(admin.ModelAdmin):
    fields = ('quem_somos', 'fale_conosco', 'termos_condicoes')
    readonly_fields = ('quem_somos', 'fale_conosco', 'termos_condicoes')

    def has_add_permission(self, request):
        # Não permitir adicionar mais instâncias
        return False

    def has_change_permission(self, request, obj=None):
        # Permitir editar a única instância
        return True

    def has_delete_permission(self, request, obj=None):
        # Não permitir excluir a única instância
        return False

admin.site.register(RedesSociais)
class RedesSociaisAdmin(admin.ModelAdmin):
    fields = ('facebook', 'instagram', 'whatsapp')
    readonly_fields = ('facebook', 'instagram', 'whatsapp')

    def has_add_permission(self, request):
        # Não permitir adicionar mais instâncias
        return False

    def has_change_permission(self, request, obj=None):
        # Permitir editar a única instância
        return True

    def has_delete_permission(self, request, obj=None):
        # Não permitir excluir a única instância
        return False

admin.site.register(Imovel, ImovelAdmin)
admin.site.register(TipoImovel)


class TipoImovelAdmin(admin.ModelAdmin):
    pass

class FotosDosImoveisAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'foto')
