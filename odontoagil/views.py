from django.shortcuts import render
#teste
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

def index(request):
    return render(request, 'index.html')

def listar_paciente(request):
    context = {
        'pacientes': PACIENTES
    }
    return render(request, 'pacientes/listar_paciente.html', context)
