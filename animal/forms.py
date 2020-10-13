from django import forms

from .models import Animai

class DateInput(forms.DateInput):
    input_type = "date"

class AnimalForm(forms.ModelForm):
    especie = forms.CharField(
        label="Espécie",
        error_messages={'max_length': 'Espécie não pode ter mais de 25 caracteres'}
    )
    sexo = forms.CharField(
        label="Sexo",
        error_messages={'max_length': 'Sobrenome não pode ter mais de 1 caracter'}
    )
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=DateInput()
    )
    descricao = forms.CharField(
        label="Descrição",
        widget=forms.Textarea 
    )
    preco = forms.DecimalField(
        label="Preço",
        max_digits=6,
        decimal_places=2
    )
    
    class Meta:
        model = Animai
        fields = (
        "especie",
        "sexo",
        "data_nascimento",
        "descricao",
        "preco"
    ) 