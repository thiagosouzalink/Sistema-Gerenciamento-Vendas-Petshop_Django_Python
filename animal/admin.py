from django.contrib import admin

# Register your models here.
from django.contrib import admin
from animal.models import Animai

# Register your models here.
class AnimaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'especie', 'sexo', 'data_nascimento', 'preco', 'mostrar')
    list_display_links = ('id', 'especie')
    search_fields = ('especie', 'preco')
    list_editable = ('mostrar',)

admin.site.register(Animai, AnimaisAdmin)