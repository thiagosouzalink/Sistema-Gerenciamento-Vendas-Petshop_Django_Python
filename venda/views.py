from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse

from venda.models import Venda
from .forms import VendaForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def venda(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/vendas.html', {
        'vendas': vendas
    })

def detalhe_venda(request, venda_id):
    # venda = Venda.objects.get(id=venda_id)
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, 'venda/detalhe_venda.html', {
        'venda': venda
    })

class VendaCreateView(CreateView):
    template_name = "venda/venda_form.html"
    form_class = VendaForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_venda")

class VendaUpdateView(UpdateView):
    template_name = "venda/venda_form.html"
    form_class = VendaForm

    def get_object(self):
        id = self.kwargs.get("venda_id")
        return get_object_or_404(Venda, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_venda")

class VendaDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("venda_id")
        return get_object_or_404(Venda, id=id)

    def get_success_url(self):
        return reverse("pg_venda")