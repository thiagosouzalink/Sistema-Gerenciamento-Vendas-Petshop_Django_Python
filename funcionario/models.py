from django.db import models
from django.urls import reverse

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    cargo = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    mostrar = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'funcionarios'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("atualizar-funcionario", kwargs={'funcionario_id':self.id})

    def get_delete_url(self):
        return reverse("deletar-funcionario", kwargs={'funcionario_id':self.id})