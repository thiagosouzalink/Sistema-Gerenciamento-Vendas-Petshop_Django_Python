from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator
from django.urls import reverse

from cliente.models import Cliente
from .forms import ClienteForm

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def cliente(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 10)
    
    page = request.GET.get('p')
    cliente = paginator.get_page(page)
    return render(request, 'cliente/clientes.html', {
        'clientes': clientes
    })

def detalhe_cliente(request, cliente_id):
    # cliente = Cliente.objects.get(id=cliente_id)
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/detalhe_cliente.html', {
            'cliente': cliente
    })
    


class ClienteCreateView(CreateView):
    template_name = "cliente/cliente_form.html"
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_cliente")

class ClienteUpdateView(UpdateView):
    template_name = "cliente/cliente_form.html"
    form_class = ClienteForm

    def get_object(self):
        id = self.kwargs.get("cliente_id")
        return get_object_or_404(Cliente, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_cliente")

class ClienteDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("cliente_id")
        return get_object_or_404(Cliente, id=id)

    def get_success_url(self):
        return reverse("pg_cliente")