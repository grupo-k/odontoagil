#
from django.urls import path, include

from .views import historia_clinica, index, listar_paciente, cadastrar_paciente, listar_procedimentos, remover_paciente, editar_paciente, detalhes_paciente, listar_usuarios
from .views import listar_servicos, cadastrar_servicos, remover_servicos, editar_servicos, detalhes_servicos
from odontoagil import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pacientes/', listar_paciente, name='listar_paciente'),
    path('pacientes/cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/remover/<int:id>/', remover_paciente, name='remover_paciente'),
    path('pacientes/editar/<int:id>/', editar_paciente, name='editar_paciente'),
    path('pacientes/detalhes/<int:id>', detalhes_paciente, name='detalhes_paciente'),
    path('historia_clinica/', historia_clinica, name='historia_clinica'),
    path('servicos/', listar_servicos, name='listar_servicos'),
    path('servicos/cadastrar/', cadastrar_servicos, name='cadastrar_servicos'),
    path('servicos/remover/<int:id>/', remover_servicos, name='remover_servicos'),
    path('servicos/editar/<int:id>/', editar_servicos, name='editar_servicos'),
    path('servicos/detalhes/<int:id>', detalhes_servicos, name='detalhes_servicos'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
]
