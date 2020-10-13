from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from funcionario.models import Funcionario
from django.urls import reverse

from funcionario.models import Funcionario
from .forms import FuncionarioForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/funcionarios.html', {
        'funcionarios': funcionarios
    })

def detalhe_funcionario(request, funcionario_id):
    # funcionario = Funcionario.objects.get(id=funcionario_id)
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionario/detalhe_funcionario.html', {
        'funcionario': funcionario
    })

class FuncionarioCreateView(CreateView):
    template_name = "funcionario/funcionario_form.html"
    form_class = FuncionarioForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_funcionario")

class FuncionarioUpdateView(UpdateView):
    template_name = "funcionario/funcionario_form.html"
    form_class = FuncionarioForm

    def get_object(self):
        id = self.kwargs.get("funcionario_id")
        return get_object_or_404(Funcionario, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_funcionario")

class FuncionarioDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("funcionario_id")
        return get_object_or_404(Funcionario, id=id)

    def get_success_url(self):
        return reverse("pg_funcionario")