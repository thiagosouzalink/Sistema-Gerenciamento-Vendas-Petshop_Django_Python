from django.contrib import admin
from venda.models import Venda

# Register your models here.
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'funcionario', 'animal', 'data_venda', 'preco', 'mostrar')
    list_display_links = ('id', 'cliente', 'funcionario', 'animal')
    search_fields = ('cliente', 'funcionario', 'animal', 'data_venda', 'preco')
    list_editable = ('mostrar',)

admin.site.register(Venda, VendaAdmin)