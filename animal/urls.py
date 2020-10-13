from django.urls import path
from . import views

urlpatterns = [
    path('animais/', views.animal, name='pg_animal'),
    path('animais/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal'),
    path('animais/inserir_animal/', views.AnimalCreateView.as_view(), name="inserir-animal"),
    path('animais/<int:animal_id>/atualizar_animal/', views.AnimalUpdateView.as_view(), name="atualizar-animal"),
    path('animais/<int:animal_id>/deletar_animal/', views.AnimalDeleteView.as_view(), name="deletar-animal"),
]