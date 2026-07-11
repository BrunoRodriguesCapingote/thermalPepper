from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('contas/', views.contas, name='contas'),
    path('receitas/', views.receitas, name='receitas'),
    path('despesas/', views.despesas, name='despesas'),
    path('produtos/', views.produtos, name='produtos'),
    path('loja/', views.loja, name='loja'),
    path('fazenda/', views.fazenda, name='fazenda'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('clientes/', views.clientes, name='clientes'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracaoUsuario/', views.configuracaoUsuario, name='configuracaoUsuario'),
]