from django.contrib import admin
from cliente.models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cpf', 'endereco', 'telefone', 'email', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')
    list_editable = ('mostrar',)

admin.site.register(Cliente, ClienteAdmin)
