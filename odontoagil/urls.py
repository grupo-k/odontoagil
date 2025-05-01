"""
URL configuration for odontoagil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import historia_clinica, index, listar_paciente, cadastrar_paciente, remover_paciente
from odontoagil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pacientes/', listar_paciente, name='listar_paciente'),
    path('pacientes/cadastrar', cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/remover/<int:id>/', remover_paciente, name='remover_paciente'),
    path('pacientes/<int:id>', index, name='editar_paciente'),
    path('pacientes/<int:id>', index, name='detalhes_paciente'),
    path('historia_clinica/', historia_clinica, name='historia_clinica'),
]
