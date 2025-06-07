from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, HistoriaClinica, Tratamento, Procedimento, Servico, Usuario

# INDEX
def index(request):
    return render(request, 'index.html')

# PACIENTES

def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_paciente.html', {'pacientes': pacientes})

def cadastrar_paciente(request):
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

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        for field in ['nome_completo', 'telefone', 'email', 'idade', 'sexo', 'data_nascimento', 'cpf',
                      'estado_civil', 'rg', 'cidade', 'estado', 'profissao', 'nome_mae', 'nome_pai',
                      'nome_contato_familiar', 'grau_parentesco', 'telefone_contato_familiar']:
            setattr(paciente, field, request.POST.get(field))
        paciente.save()
        return redirect('listar_paciente')

    return render(request, 'pacientes/editar_paciente.html', {'paciente': paciente})

def remover_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_paciente')

def detalhes_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    return render(request, 'pacientes/detalhes_paciente.html', {'paciente': paciente})

# HISTÓRIA CLÍNICA

def historia_clinica(request):
    pacientes = Paciente.objects.prefetch_related('historias_clinicas').all()
    # Isso carrega pacientes com as histórias clínicas associadas de forma eficiente

    context = {
        'pacientes': pacientes
    }
    return render(request, 'historia_clinica/historia_clinica.html', context)

#cadastrar_historia_clinica
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, HistoriaClinica
from django.utils import timezone

def cadastrar_historia_clinica(request, paciente_id):
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

def editar_historia_clinica(request, paciente_id, historia_id):
    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente_id=paciente_id)

    if request.method == 'POST':
        for field in ['motivo', 'diagnostico', 'tratamento', 'recomendacoes']:
            setattr(historia, field, request.POST.get(field))
        historia.save()
        return redirect('historia_clinica')

    paciente = historia.paciente
    return render(request, 'historia_clinica/editar_historia_clinica.html', {'historia': historia, 'paciente': paciente})

def remover_historia_clinica(request, paciente_id, historia_id):
    # Busca o paciente e a história clínica correspondentes
    paciente = get_object_or_404(Paciente, id=paciente_id)
    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente=paciente)
    
    # Exclui a história clínica
    historia.delete()
    
    # Redireciona de volta para a lista de histórias clínicas ou outra página desejada
    return redirect('historia_clinica')

#detalhes_historia_clinica
def detalhes_historia_clinica(request, paciente_id, historia_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    historia = get_object_or_404(HistoriaClinica, id=historia_id, paciente=paciente)
    context = {
        'paciente': paciente,
        'historia': historia,
    }
    return render(request, 'historia_clinica/detalhes_historia_clinica.html', context)

# TRATAMENTOS

def tratamentos(request):
    tratamentos = Tratamento.objects.select_related('paciente').all()
    return render(request, 'tratamentos/tratamentos.html', {'tratamentos': tratamentos})

# PROCEDIMENTOS

def listar_procedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimentos/listar_procedimentos.html', {'procedimentos': procedimentos})

# SERVIÇOS

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/listar_servicos.html', {'servicos': servicos})

def cadastrar_servicos(request):
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
        return redirect('listar_servicos')  # ou outra URL que queira após cadastro

    return render(request, 'servicos/cadastrar_servicos.html')

def editar_servicos(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        for field in ['data_inclusao', 'codigo_servicos', 'material_usado', 'descricao_servicos',
                      'codigo_servicos_secundario', 'descricao_servicos_secundario', 'aparelho_apoio',
                      'observacoes']:
            setattr(servico, field, request.POST.get(field))
        servico.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/editar_servicos.html', {'servico': servico})

def remover_servicos(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    return redirect('listar_servicos')

def detalhes_servicos(request, id):
    servico = get_object_or_404(Servico, id=id)
    return render(request, 'servicos/detalhes_servicos.html', {'servico': servico})


# USUÁRIOS

def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # nome mais descritivo (plural)
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})


def cadastrar_usuario(request):
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


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.cargo = request.POST.get('cargo')
        usuario.save()
        return redirect('listar_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})


def remover_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuarios')


def detalhes_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'usuarios/detalhes_usuario.html', {'usuario': usuario})
