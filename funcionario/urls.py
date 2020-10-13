from django.urls import path
from . import views

urlpatterns = [
    path('funcionarios/', views.funcionario, name='pg_funcionario'),
    path('funcionarios/<int:funcionario_id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('funcionarios/inserir_funcionario/', views.FuncionarioCreateView.as_view(), name="inserir-funcionario"),
    path('funcionarios/<int:funcionario_id>/atualizar_funcionario/', views.FuncionarioUpdateView.as_view(), name="atualizar-funcionario"),
    path('funcionarios/<int:funcionario_id>/deletar_funcionario/', views.FuncionarioDeleteView.as_view(), name="deletar-funcionario"),
]