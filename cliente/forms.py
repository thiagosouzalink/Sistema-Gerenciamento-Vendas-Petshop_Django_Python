from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome",
        error_messages={'max_length': 'Nome não pode ter mais de 25 caracteres'}
    )
    sobrenome = forms.CharField(
        label="Sobrenome",
        error_messages={'max_length': 'Sobrenome não pode ter mais de 25 caracteres'}
    )
    cpf = forms.CharField(
        label="CPF",
        error_messages={'max_length': 'CPF não pode ter mais de 14 caracteres'}
    )
    endereco = forms.CharField(
        label="Endereço", 
        error_messages={'max_length': 'Nome não pode ter mais de 30 caracteres'}
    )
    telefone = forms.CharField(
        label="Telefone",
        error_messages={"max_length": "Número de telefone não pode ter mais de 20 caracteres"}
    )
    email = forms.EmailField(
        label="E-mail"
    )
    
    class Meta:
        model = Cliente
        fields = (
        "nome", 
        "sobrenome", 
        "cpf", 
        "endereco", 
        "telefone", 
        "email",
    ) 
    