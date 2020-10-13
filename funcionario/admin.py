from django.contrib import admin
from funcionario.models import Funcionario

# Register your models here.
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cargo', 'email', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'cargo', 'email')
    list_editable = ('mostrar',)

admin.site.register(Funcionario, FuncionarioAdmin)