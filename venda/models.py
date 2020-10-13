from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from cliente.models import Cliente
from funcionario.models import Funcionario
from animal.models import Animai


# Create your models here.
class Venda(models.Model):
    def get_sentinel_user():
        return get_user_model().objects.get_or_create(username='deleted')[0]

    cliente = models.ForeignKey(Cliente, on_delete=models.SET(get_sentinel_user))
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET(get_sentinel_user))
    animal = models.ForeignKey(Animai, on_delete=models.SET(get_sentinel_user))
    data_venda = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    mostrar = models.BooleanField(default=True)

    class Meta:
        db_table = 'vendas'

    def get_absolute_url(self):
        return reverse("atualizar-venda", kwargs={'venda_id':self.id})

    def get_delete_url(self):
        return reverse("deletar-venda", kwargs={'venda_id':self.id})