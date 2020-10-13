from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models

# Create your models here.
class Animai(models.Model):
    especie = models.CharField(max_length=25)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    mostrar = models.BooleanField(default=True)

    class Meta:
        db_table = 'animais'

    def __str__(self):
        return self.especie

    def get_absolute_url(self):
        return reverse("atualizar-animal", kwargs={'animal_id':self.id})

    def get_delete_url(self):
        return reverse("deletar-animal", kwargs={'animal_id':self.id})