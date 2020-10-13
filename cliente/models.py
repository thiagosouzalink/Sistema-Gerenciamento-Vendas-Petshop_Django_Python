from django.db import models
from django.urls import reverse


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    mostrar = models.BooleanField(default=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("atualizar-cliente", kwargs={'cliente_id':self.id})

    def get_delete_url(self):
        return reverse("deletar-cliente", kwargs={'cliente_id':self.id})