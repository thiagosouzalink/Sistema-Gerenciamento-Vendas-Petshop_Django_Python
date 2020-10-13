from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.venda, name='pg_venda'),
    path('vendas/<int:venda_id>/', views.detalhe_venda, name='detalhe_venda'),
    path('vendas/inserir_venda/', views.VendaCreateView.as_view(), name="inserir-venda"),
    path('vendas/<int:venda_id>/atualizar_venda/', views.VendaUpdateView.as_view(), name="atualizar-venda"),
    path('vendas/<int:venda_id>/deletar_venda/', views.VendaDeleteView.as_view(), name="deletar-venda"),
]