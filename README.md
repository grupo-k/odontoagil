# OdontoÁgil 🦷  
Desenvolvimento do projeto OdontoÁgil do TADS da UDESC

## ✨ Criado em  
18 de abril de 2025

## 👥 Integrantes  
- Ana Laura Coan  
- Carlos Alberto Zapelini Farias  
- Michel Luiz Ayres Pontes Junior  
- Pablo Idalgo Gonzelez

---

## 🚨 Arquivos Importantes

- **Protótipo de Interfaces (Programação Web)**  
  [https://grupo-k.github.io/ad1_programacao_web/pages/pacientes_analaura/index_pacientes.html](https://grupo-k.github.io/ad1_programacao_web/pages/pacientes_analaura/index_pacientes.html)

- **Documento de Requisitos**  
  [https://docs.google.com/document/d/1vemgy5_uxrecuBW98eCzRCLMhwTpBkFL8qJQb1j0ptw](https://docs.google.com/document/d/1vemgy5_uxrecuBW98eCzRCLMhwTpBkFL8qJQb1j0ptw)

- **Design UX**  
  [https://drive.google.com/file/d/1BP-TEFG3OshKWXpdBr9KGKHOmmIHTkIv](https://drive.google.com/file/d/1BP-TEFG3OshKWXpdBr9KGKHOmmIHTkIv)

---

## ✅ Funcionalidades

### 📁 Módulo: Pacientes
- Cadastro de novo paciente
- Listagem de pacientes cadastrados
- Edição de dados do paciente
- Remoção de paciente

### 🩺 Módulo: História Clínica
- Cadastro de histórico clínico
- Listagem de históricos do paciente
- Edição de histórico
- Remoção de histórico

### 🦷 Módulo: Tratamentos
- Cadastro de tratamento
- Listagem de tratamentos do paciente
- Edição de tratamento
- Remoção de tratamento

### 🛠️ Módulo: Procedimentos
- Cadastro de procedimento
- Listagem de procedimentos por tratamento
- Edição de procedimento
- Remoção de procedimento

---

## 🗂️ Quadro Kanban

| 📝 To Do | 🚧 Doing | ✅ Done |
|---------|----------|--------|
| Criar view `listar_pacientes` | | ✅ |
| Criar rota `/pacientes/` | | ✅ |
| Desenvolver template `listar_pacientes.html` | 🚧 | |
| Implementar ações: Editar, Remover | | |
| Criar view `cadastrar_paciente` | | |
| Criar formulário de cadastro com validação | | |
| Criar rota `/pacientes/novo/` | | |
| Criar view `editar_paciente` | | |
| Criar rota `/pacientes/editar/<id>/` | | |
| Criar view `remover_paciente` | | |
| Criar rota `/pacientes/remover/<id>/` | | |
| Criar view `listar_historia_clinica` | 🚧 | |
| Criar rota `/historias/` | | |
| Criar template `listar_historia_clinica.html` | | |
| Implementar ações: Editar, Remover | | |
| Criar view `cadastrar_historia_clinica` | | |
| Criar rota `/historias/novo/<paciente_id>/` | | |
| Criar formulário com validações | | |
| Criar view `editar_historia_clinica` | | |
| Criar rota `/historias/editar/<id>/` | | |
| Criar view `remover_historia_clinica` | | |
| Criar rota `/historias/remover/<id>/` | | |
| Criar model `Tratamento` | | |
| Criar view `listar_tratamentos` | | |
| Criar rota `/tratamentos/` | | |
| Criar template `listar_tratamentos.html` | | |
| Implementar ações: Editar, Remover | | |
| Criar view `cadastrar_tratamento` | | |
| Criar rota `/tratamentos/novo/<paciente_id>/` | | |
| Criar formulário com validações | | |
| Criar view `editar_tratamento` | | |
| Criar rota `/tratamentos/editar/<id>/` | | |
| Criar view `remover_tratamento` | | |
| Criar rota `/tratamentos/remover/<id>/` | | |
| Criar model `Procedimento` | | |
| Criar view `listar_procedimentos` | | |
| Criar rota `/procedimentos/` | | |
| Criar template `listar_procedimentos.html` | | |
| Criar view `cadastrar_procedimento` | | |
| Criar rota `/procedimentos/novo/<tratamento_id>/` | | |
| Criar formulário com validações | | |
| Criar view `editar_procedimento` | | |
| Criar rota `/procedimentos/editar/<id>/` | | |
| Criar view `remover_procedimento` | | |
| Criar rota `/procedimentos/remover/<id>/` | | |

---

## 📌 Tecnologias utilizadas

- Python / Django
- HTML / CSS (Responsivo)
