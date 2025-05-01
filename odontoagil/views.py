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
        'cpf': '123.456.789-00'
    },
    {
        'id': 2,
        'nome_completo': 'Carlos Silva',
        'telefone': '(11) 98765-4321',
        'email': 'carlos@exemplo.com',
        'idade': 45,
        'sexo': 'Masculino',
        'data_nascimento': '1980-10-15',
        'cpf': '987.654.321-00'
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
