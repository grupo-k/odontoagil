from django.shortcuts import render

PACIENTES = [
    {
        'nome_completo': 'Ana Laura Coan',
        'telefone': '(11) 12345-6789',
        'email': 'ana@exemplo.com',
        'idade': 30,
        'sexo': 'Feminino',
        'data_nascimento': '1994-03-20'
    },
    {
        'nome_completo': 'Carlos Silva',
        'telefone': '(11) 98765-4321',
        'email': 'carlos@exemplo.com',
        'idade': 45,
        'sexo': 'Masculino',
        'data_nascimento': '1980-10-15'
    },
]

def index(request):
    return render(request, 'index.html')

def paciente_list(request):
    context = {
        'pacientes': PACIENTES
    }
    return render(request, 'paciente_list.html', context)
