from django import forms

from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = (
            'cliente',
            'funcionario',
            'animal',
            'data_venda',
            'preco'
        )

    class DateInput(forms.DateInput):
        input_type = "date"

    data_venda = forms.DateField(
        label="Data da Venda",
        widget=DateInput()
    )
    preco = forms.DecimalField(
        label="Preço",
        max_digits=6,
        decimal_places=2
    )