from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse

from animal.models import Animai
from .forms import AnimalForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def animal(request):
    animais = Animai.objects.all()
    return render(request, 'animal/animais.html', {
        'animais': animais
    })

def detalhe_animal(request, animal_id):
    # animal = Animai.objects.get(id=animal_id)
    animal = get_object_or_404(Animai, id=animal_id)
    return render(request, 'animal/detalhe_animal.html', {
        'animal': animal
    })

class AnimalCreateView(CreateView):
    template_name = "animal/animal_form.html"
    form_class = AnimalForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_animal")

class AnimalUpdateView(UpdateView):
    template_name = "animal/animal_form.html"
    form_class = AnimalForm

    def get_object(self):
        id = self.kwargs.get("animal_id")
        return get_object_or_404(Animai, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pg_animal")

class AnimalDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("animal_id")
        return get_object_or_404(Animai, id=id)

    def get_success_url(self):
        return reverse("pg_animal")