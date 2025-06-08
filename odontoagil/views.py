from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, HistoriaClinica, Tratamento, Procedimento, Servico, Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone

# INDEX
def index(request):
    return render(request, 'index.html')

# PACIENTES

@login_required
def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_paciente.html', {'pacientes': pacientes})

@login_required
def cadastrar_paciente(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para cadastrar pacientes.")
    
    if request.method == 'POST':
        paciente = Paciente(
            nome_completo=request.POST.get('nome_completo'),
            telefone=request.POST.get('telefone'),
            email=request.POST.get('email'),
            idade=request.POST.get('idade'),
            sexo=request.POST.get('sexo'),
            data_nascimento=request.POST.get('data_nascimento'),
            cpf=request.POST.get('cpf'),
            estado_civil=request.POST.get('estado_civil', ''),
            rg=request.POST.get('rg', ''),
            cidade=request.POST.get('cidade', ''),
            estado=request.POST.get('estado', ''),
            profissao=request.POST.get('profissao', ''),
            nome_mae=request.POST.get('nome_mae', ''),
            nome_pai=request.POST.get('nome_pai', ''),
            nome_contato_familiar=request.POST.get('nome_contato_familiar', ''),
            grau_parentesco=request.POST.get('grau_parentesco', ''),
            telefone_contato_familiar=request.POST.get('telefone_contato_familiar', '')
        )
        paciente.save()
        return redirect('listar_paciente')

    return render(request, 'pacientes/cadastrar_paciente.html')

@login_required
def editar_paciente(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para editar pacientes.")
    
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        for field in ['nome_completo', 'telefone', 'email', 'idade', 'sexo', 'data_nascimento', 'cpf',
                      'estado_civil', 'rg', 'cidade', 'estado', 'profissao', 'nome_mae', 'nome_pai',
                      'nome_contato_familiar', 'grau_parentesco', 'telefone_contato_familiar']:
            setattr(paciente, field, request.POST.get(field))
        paciente.save()
        return redirect('listar_paciente')

    return render(request, 'pacientes/editar_paciente.html', {'paciente': paciente})

@login_required
def remover_paciente(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para remover pacientes.")
    
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_paciente')

@login_required
def detalhes_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    return render(request, 'pacientes/detalhes_paciente.html', {'paciente': paciente})

# HISTÓRIA CLÍNICA

@login_required
def historia_clinica(request):
    pacientes = Paciente.objects.prefetch_related('historias_clinicas').all()
    context = {
        'pacientes': pacientes
    }
    return render(request, 'historia_clinica/historia_clinica.html', context)

@login_required
def cadastrar_historia_clinica(request, paciente_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para cadastrar história clínica.")

    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        motivo = request.POST.get('motivo', '')
        diagnostico = request.POST.get('diagnostico', '')
        tratamento = request.POST.get('tratamento', '')
        recomendacoes = request.POST.get('recomendacoes', '')

        HistoriaClinica.objects.create(
            paciente=paciente,
            motivo=motivo,
            diagnostico=diagnostico,
            tratamento=tratamento,
            recomendacoes=recomendacoes,
            data_criacao=timezone.now()
        )

        return redirect('historia_clinica')

    return render(request, 'historia_clinica/cadastrar_historia_clinica.html', {'paciente': paciente})

@login_required
def editar_historia_clinica(request, paciente_id, historia_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para editar história clínica.")

    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente_id=paciente_id)

    if request.method == 'POST':
        for field in ['motivo', 'diagnostico', 'tratamento', 'recomendacoes']:
            setattr(historia, field, request.POST.get(field))
        historia.save()
        return redirect('historia_clinica')

    paciente = historia.paciente
    return render(request, 'historia_clinica/editar_historia_clinica.html', {'historia': historia, 'paciente': paciente})

@login_required
def remover_historia_clinica(request, paciente_id, historia_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para remover história clínica.")

    paciente = get_object_or_404(Paciente, id=paciente_id)
    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente=paciente)
    historia.delete()
    return redirect('historia_clinica')

@login_required
def detalhes_historia_clinica(request, paciente_id, historia_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente=paciente)
    context = {
        'paciente': paciente,
        'historia': historia,
    }
    return render(request, 'historia_clinica/detalhes_historia_clinica.html', context)

# TRATAMENTOS

@login_required
def tratamentos(request):
    tratamentos = Tratamento.objects.select_related('paciente').all()
    return render(request, 'tratamentos/tratamentos.html', {'tratamentos': tratamentos})

# PROCEDIMENTOS

@login_required
def listar_procedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimentos/listar_procedimentos.html', {'procedimentos': procedimentos})

# SERVIÇOS

@login_required
def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/listar_servicos.html', {'servicos': servicos})

@login_required
def cadastrar_servicos(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para cadastrar serviços.")

    if request.method == 'POST':
        codigo_servicos = request.POST.get('codigo_servicos')
        material_usado = request.POST.get('material_usado')
        descricao_servicos = request.POST.get('descricao_servicos')
        codigo_servicos_secundario = request.POST.get('codigo_servicos_secundario')
        descricao_servicos_secundario = request.POST.get('descricao_servicos_secundario')
        aparelho_apoio = request.POST.get('aparelho_apoio')
        observacoes = request.POST.get('observacoes')

        servico = Servico(
            codigo_servicos=codigo_servicos,
            material_usado=material_usado,
            descricao_servicos=descricao_servicos,
            codigo_servicos_secundario=codigo_servicos_secundario,
            descricao_servicos_secundario=descricao_servicos_secundario,
            aparelho_apoio=aparelho_apoio,
            observacoes=observacoes
        )
        servico.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/cadastrar_servicos.html')

@login_required
def editar_servicos(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para editar serviços.")

    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        for field in ['data_inclusao', 'codigo_servicos', 'material_usado', 'descricao_servicos',
                      'codigo_servicos_secundario', 'descricao_servicos_secundario', 'aparelho_apoio',
                      'observacoes']:
            setattr(servico, field, request.POST.get(field))
        servico.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/editar_servicos.html', {'servico': servico})

@login_required
def remover_servicos(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para remover serviços.")

    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    return redirect('listar_servicos')

@login_required
def detalhes_servicos(request, id):
    servico = get_object_or_404(Servico, id=id)
    return render(request, 'servicos/detalhes_servicos.html', {'servico': servico})

# USUÁRIO

@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

@login_required
def cadastrar_usuario(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para cadastrar usuários.")

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')

        Usuario.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            cargo=cargo
        )
        return redirect('listar_usuarios')

    return render(request, 'usuarios/cadastrar_usuario.html')

@login_required
def editar_usuario(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para editar usuários.")

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.cargo = request.POST.get('cargo')
        usuario.save()
        return redirect('listar_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

@login_required
def remover_usuario(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para remover usuários.")

    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuarios')

@login_required
def detalhes_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'usuarios/detalhes_usuario.html', {'usuario': usuario})
