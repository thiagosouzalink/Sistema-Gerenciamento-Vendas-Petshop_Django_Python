
from django import forms

from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome",
        error_messages={'max_length': 'Nome não pode ter mais de 25 caracteres'}
    )
    sobrenome = forms.CharField(
        label="Sobrenome",
        error_messages={'max_length': 'Sobrenome não pode ter mais de 25 caracteres'}
    )
    cargo = forms.CharField(
        label="Cargo",
        error_messages={'max_length': 'Cargo não pode ter mais de 25 caracteres'}
    )
    email = forms.EmailField(
        label="E-mail"
    )
    
    class Meta:
        model = Funcionario
        fields = (
        "nome",
        "sobrenome",
        "cargo",
        "email"
    ) 