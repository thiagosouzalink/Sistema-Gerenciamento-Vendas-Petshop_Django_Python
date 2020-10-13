from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente, name='pg_cliente'),
    path('clientes/<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('clientes/inserir_cliente/', views.ClienteCreateView.as_view(), name="inserir-cliente"),
    path('clientes/<int:cliente_id>/atualizar_cliente/', views.ClienteUpdateView.as_view(), name="atualizar-cliente"),
    path('clientes/<int:cliente_id>/deletar_cliente/', views.ClienteDeleteView.as_view(), name="deletar-cliente"),
]