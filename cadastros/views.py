from django.shortcuts import redirect, render

# Dados dos pacientes
PACIENTES = [
    {
        'id': 1,
        'nome_completo': 'Ana Laura Coan',
        'telefone': '(11) 12345-6789',
        'email': 'ana@exemplo.com',
        'idade': 30,
        'sexo': 'Feminino',
        'data_nascimento': '1994-03-20',
        'cpf': '123.456.789-00',
        'estado_civil': 'Solteira',
        'rg': '12.345.678-9',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'profissao': 'Dentista',
        'nome_mae': 'Maria Coan',
        'nome_pai': 'João Coan',
        'nome_contato_familiar': 'Pedro Coan',
        'grau_parentesco': 'Irmão',
        'telefone_contato_familiar': '(11) 23456-7890'
    },
    {
        'id': 2,
        'nome_completo': 'Carlos Silva',
        'telefone': '(11) 98765-4321',
        'email': 'carlos@exemplo.com',
        'idade': 45,
        'sexo': 'Masculino',
        'data_nascimento': '1980-10-15',
        'cpf': '987.654.321-00',
        'estado_civil': 'Casado',
        'rg': '98.765.432-1',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'profissao': 'Engenheiro',
        'nome_mae': 'Ana Silva',
        'nome_pai': 'Carlos Silva',
        'nome_contato_familiar': 'Paulo Silva',
        'grau_parentesco': 'Filho',
        'telefone_contato_familiar': '(11) 98765-4322'
    },
]

# Histórias clínicas associadas aos pacientes
HISTORIAS_CLINICAS = [
    {
        'paciente_id': 1,
        'data_consulta': '2025-04-10',
        'motivo': 'Dor de dente constante no lado inferior esquerdo.',
        'diagnostico': 'Cárie em estágio avançado no molar 36.',
        'tratamento': 'Remoção da cárie e restauração com resina composta.',
        'recomendacoes': 'Retorno em 6 meses e higiene bucal com fio dental.'
    },
    {
        'paciente_id': 2,
        'data_consulta': '2025-04-12',
        'motivo': 'Avaliação de rotina e limpeza.',
        'diagnostico': 'Tártaro na região inferior anterior.',
        'tratamento': 'Profilaxia com ultrassom e aplicação de flúor.',
        'recomendacoes': 'Escovar os dentes 3x ao dia e retornar em 6 meses.'
    },
]

# Dados simulados de tratamentos
TRATAMENTOS = [
    {
        'id': 1,
        'paciente_id': 1,
        'descricao': 'Canal no molar inferior esquerdo',
        'data': '2025-05-01',
    },
    {
        'id': 2,
        'paciente_id': 2,
        'descricao': 'Extração de siso',
        'data': '2025-04-28',
    },
]

# Dados simulados de procedimentos e preços
PROCEDIMENTOS = [
    {
        'id': 1,
        'nome': 'Restauração',
        'descricao': 'Tratamento de cáries com resina composta.',
        'preco': 250.00,
    },
    {
        'id': 2,
        'nome': 'Limpeza',
        'descricao': 'Limpeza profissional dos dentes com ultrassom.',
        'preco': 120.00,
    },
    {
        'id': 3,
        'nome': 'Extração de dente',
        'descricao': 'Extração simples de dente.',
        'preco': 300.00,
    },
]

# Dados dos serviços
SERVICOS = [
    {
        'id': 1,
        'data_inclusao': '18/05/2025',
        'codigo_servicos': 'cod01',
        'material_usado': 'Bicarbonato, extratores de tártaro, curetas e ultrassom odontológico e flúor2.',
        'descricao_servicos': 'Limpeza Dental - Remoção de placa bacteriana, tártaro e manchas dos dentes.',
        'codigo_servicos_secundario': 'cod02',
        'descricao_servicos_secundario': 'Polimento e aplicação de flúor2.',
        'aparelho_apoio': 'Jatos de bicarbonato.',
        'Observacoes': 'Essa limpeza visa prevenir problemas como cárie, placa bacteriana e gengivite.',
        },
    {
        'id': 2,
        'data_inclusao': '18 maio 2025',
        'codigo_servicos': 'cod03',
        'material_usado': 'Bicarbonato, extratores de tártaro, curetas e ultrassom odontológico e flúor2.',
        'descricao_servicos': 'Limpeza Dental - Remoção de placa bacteriana, tártaro e manchas dos dentes.',
        'codigo_servicos_secundario': 'cod04',
        'descricao_servicos_secundário': 'Polimento e aplicação de flúor2.',
        'aparelho_apoio': 'Jatos de bicarbonato.',
        'observacoes': 'Essa limpeza visa prevenir problemas como cárie, placa bacteriana e gengivite.',
    },
]

USUARIOS = [
    {
        'id': 1,
        'nome_completo': 'João Admin',
        'email': 'joao.admin@exemplo.com',
        'telefone': '(11) 99999-1234',
        'cpf': '111.222.333-44',
    },
    {
        'id': 2,
        'nome_completo': 'Maria Secretaria',
        'email': 'maria.secretaria@exemplo.com',
        'telefone': '(11) 98888-5678',
        'cpf': '555.666.777-88',
    },
]

def index(request):
    return render(request, 'index.html')

# PACIENTES

# Listar Pacientes

def listar_paciente(request):
    context = {
        'pacientes': PACIENTES
    }
    return render(request, 'pacientes/listar_paciente.html', context)

# Cadastrar Paciente

def cadastrar_paciente(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')

        estado_civil = request.POST.get('estado_civil', '')
        rg = request.POST.get('rg', '')
        cidade = request.POST.get('cidade', '')
        estado = request.POST.get('estado', '')
        profissao = request.POST.get('profissao', '')
        nome_mae = request.POST.get('nome_mae', '')
        nome_pai = request.POST.get('nome_pai', '')
        nome_contato_familiar = request.POST.get('nome_contato_familiar', '')
        grau_parentesco = request.POST.get('grau_parentesco', '')
        telefone_contato_familiar = request.POST.get('telefone_contato_familiar', '')

        novo_paciente = {
            'id': len(PACIENTES) + 1,
            'nome_completo': nome_completo,
            'telefone': telefone,
            'email': email,
            'idade': idade,
            'sexo': sexo,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'estado_civil': estado_civil,
            'rg': rg,
            'cidade': cidade,
            'estado': estado,
            'profissao': profissao,
            'nome_mae': nome_mae,
            'nome_pai': nome_pai,
            'nome_contato_familiar': nome_contato_familiar,
            'grau_parentesco': grau_parentesco,
            'telefone_contato_familiar': telefone_contato_familiar
        }

        PACIENTES.append(novo_paciente)
        return redirect('listar_paciente')

    return render(request, 'pacientes/cadastrar_paciente.html')

## Remover Paciente

def remover_paciente(request, id):
    global PACIENTES
    PACIENTES = [p for p in PACIENTES if p['id'] != id]
    return redirect('listar_paciente')

## Editar Paciente

def editar_paciente(request, id):
    paciente = next((p for p in PACIENTES if p['id'] == id), None)

    if paciente is None:
        return redirect('listar_paciente')  
    
    if request.method == 'POST':
        paciente['nome_completo'] = request.POST.get('nome_completo')
        paciente['telefone'] = request.POST.get('telefone')
        paciente['email'] = request.POST.get('email')
        paciente['idade'] = int(request.POST.get('idade'))
        paciente['sexo'] = request.POST.get('sexo')
        paciente['data_nascimento'] = request.POST.get('data_nascimento')
        paciente['cpf'] = request.POST.get('cpf')
        paciente['estado_civil'] = request.POST.get('estado_civil')
        paciente['rg'] = request.POST.get('rg')
        paciente['cidade'] = request.POST.get('cidade')
        paciente['estado'] = request.POST.get('estado')
        paciente['profissao'] = request.POST.get('profissao')
        paciente['nome_mae'] = request.POST.get('nome_mae')
        paciente['nome_pai'] = request.POST.get('nome_pai')
        paciente['nome_contato_familiar'] = request.POST.get('nome_contato_familiar')
        paciente['grau_parentesco'] = request.POST.get('grau_parentesco')
        paciente['telefone_contato_familiar'] = request.POST.get('telefone_contato_familiar')

        return redirect('listar_paciente')

    return render(request, 'pacientes/editar_paciente.html', {'paciente': paciente})

## Detalhes Paciente

def detalhes_paciente(request, id):
    paciente = next((p for p in PACIENTES if p['id'] == id), None)
    
    if paciente is None:
        return redirect('listar_paciente')  

    context = {
        'paciente': paciente
    }

    return render(request, 'pacientes/detalhes_paciente.html', context)

# HISTÓRIA CLÍNICA

def historia_clinica(request):
    pacientes_com_historia = []

    for paciente in PACIENTES:
        historia = next((h for h in HISTORIAS_CLINICAS if h['paciente_id'] == paciente['id']), None)
        if historia:
            paciente_copy = paciente.copy()
            paciente_copy.update(historia)
            pacientes_com_historia.append(paciente_copy)

    context = {
        'pacientes': pacientes_com_historia
    }
    return render(request, 'historia_clinica/historia_clinica.html', context)

def tratamentos(request):
    tratamentos_com_pacientes = []
    for t in TRATAMENTOS:
        paciente = next((p for p in PACIENTES if p['id'] == t['paciente_id']), None)
        if paciente:
            tratamento = t.copy()
            tratamento['paciente_nome'] = paciente['nome_completo']
            tratamentos_com_pacientes.append(tratamento)

    return render(request, 'tratamentos/tratamentos.html', {'tratamentos': tratamentos_com_pacientes})

def listar_procedimentos(request):
    context = {
        'procedimentos': PROCEDIMENTOS
    }
    return render(request, 'procedimentos/listar_procedimentos.html', context)

# SERVIÇOS

# Listar Serviços

def listar_servicos(request):
    context = {
        'servicos': SERVICOS
    }
    return render(request, 'servicos/listar_servicos.html', context)

# Cadastrar Serviços

def cadastrar_servicos(request):
    if request.method == 'POST':
        data_inclusao = request.POST.get('data_inclusao')
        codigo_servicos = request.POST.get('codigo_servicos')
        material_usado = request.POST.get('material_usado')
        descricao_servicos = request.POST.get('descricao_servvicos')
        codigo_servicos_secundario = request.POST.get('codigo_servicos_secundario')
        descricao_servicos_secundario = request.POST.get('descricao_servicos_secundario')
        aparelho_apoio = request.POST.get('aparelho_apoio')
        observacoes = request.POST.get('observacoes')

        novo_servicos = {
            'id': len(SERVICOS) + 1,
            'data_inclusao': data_inclusao,
            'codigo_servicos': codigo_servicos,
            'material_usado' : material_usado,
            'descricao_servicos' : descricao_servvicos,
            'codigo_servicos_secundario' : codigo_servicos_secundario,
            'descricao_servicos_secundario' : descricao_servicos_secundario,
            'aparelho_apoio' : aparelho_apoio,
            'observacoes' : observacoes,
            }

        SERVICOS.append(novo_servicos)
        return redirect('listar_servicos')

    return render(request, 'servicos/cadastrar_servicos.html')

## Remover Serviços

def remover_servicos(request, id):
    global SERVICOS
    SERVICOS = [s for s in SERVICOS if s['id'] != id]
    return redirect('listar_servicos')

## Editar Serviços
def editar_servicos(request, id):
    servicos = next((s for s in SERVICOS if s['id'] == id), None)

    if servicos is None:
        return redirect('listar_servicos')  
    
    if request.method == 'POST':
        servico['data_inclusao'] = request.POST.get('data_inclusao')
        servico['codigo_servicos'] = request.POST.get('codigo_servicos')
        servico['material_usado'] = request.POST.get('material_usado')
        servico['descricao_servicos'] = request.POST.get('descricao_servicos')
        servico['codigo_servicos_secundario'] = request.POST.get('codigo_servicos_secundario')
        servico['descricao_servicos_secundario'] = request.POST.get('descricao_servicos_secundario')
        servico['aparelho_apoio'] = request.POST.get('aparelho_apoio')
        servico['observacoes'] = request.POST.get('observacoes')
        return redirect('listar_servicos')

    return render(request, 'servicos/editar_servicos.html', {'servicos': servicos})

## Detalhes Serviços

def detalhes_servicos(request, id):
    servicos = next((s for s in SERVICOS if s['id'] == id), None)
    
    if servicos is None:
        return redirect('listar_servicos')  

    context = {
        'servicos': servicos
    }

    return render(request, 'servicos/detalhes_servicos.html', context)

# LISTAR USUÁRIOS
def listar_usuarios(request):
    context = {
        'usuarios': USUARIOS
    }
    return render(request, 'usuarios/listar_usuarios.html', context)


# Create your views here.
