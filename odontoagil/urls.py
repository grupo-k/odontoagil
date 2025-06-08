from django.contrib import admin
from django.urls import path
from odontoagil import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Pacientes
    path('pacientes/', views.listar_paciente, name='listar_paciente'),
    path('pacientes/cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/remover/<int:id>/', views.remover_paciente, name='remover_paciente'),
    path('pacientes/detalhes/<int:id>/', views.detalhes_paciente, name='detalhes_paciente'),

   # História Clínica
    path('historia_clinica/', views.historia_clinica, name='historia_clinica'),
    path('historia_clinica/cadastrar/<int:paciente_id>/', views.cadastrar_historia_clinica, name='cadastrar_historia_clinica'),  # Nova rota
    path('historia_clinica/editar/<int:paciente_id>/<int:historia_id>/', views.editar_historia_clinica, name='editar_historia_clinica'),
    path('historia_clinica/remover/<int:paciente_id>/<int:historia_id>/', views.remover_historia_clinica, name='remover_historia_clinica'),
    path('historia_clinica/detalhes/<int:paciente_id>/<int:historia_id>/', views.detalhes_historia_clinica, name='detalhes_historia_clinica'),

    # Serviços
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    path('servicos/cadastrar/', views.cadastrar_servicos, name='cadastrar_servicos'),
    path('servicos/editar/<int:id>/', views.editar_servicos, name='editar_servicos'),
    path('servicos/remover/<int:id>/', views.remover_servicos, name='remover_servicos'),
    path('servicos/detalhes/<int:id>/', views.detalhes_servicos, name='detalhes_servicos'),

    # Usuários
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/remover/<int:id>/', views.remover_usuario, name='remover_usuario'),
    path('usuarios/detalhes/<int:id>/', views.detalhes_usuario, name='detalhes_usuario'),

]
