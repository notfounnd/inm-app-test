import json
from django.contrib import messages
from django.shortcuts import render, redirect
import requests
from requests.auth import HTTPBasicAuth
# Create your views here.

def lista_empregados(request):
    if request.user.is_authenticated:
        response = requests.get("https://inm-api-test.herokuapp.com/empregado/list_all", auth=HTTPBasicAuth('inmetrics', 'automacao'))
        empregados = response.json()
        return render(request, 'empregados/lista_empregados.html', {'empregados': empregados })
    else:
        return redirect('login')

def edit(request, emp_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST['nome']
            admissao = request.POST['admissao']
            cargo = request.POST['cargo']
            sexo = request.POST['sexo']
            cpf = request.POST['cpf']
            salario = request.POST['salario']
            tipo_contratacao = request.POST['tipo-contratacao']
            response = edita_empregado(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao, emp_id)
            if response.status_code == 202:
                messages.success(request, 'Informações atualizadas com sucesso')
                return redirect('lista_empregados')
            else:
                messages.error(request, 'Ops.. Não conseguimos atualizar as informações')
                return redirect('lista_empregados')
        else:
            empregado = busca_empregado(emp_id)
            return render(request, 'empregados/edit.html', {'empregado': empregado})
    else:
        return redirect('login')

def new_empregado(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST['nome']
            admissao = request.POST['admissao']
            cargo = request.POST['cargo']
            sexo = request.POST['sexo']
            cpf = request.POST['cpf']
            salario = request.POST['salario']
            tipo_contratacao = request.POST['tipo-contratacao']
            response = cadastra_empregado(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao)
            if response.status_code == 202:
                messages.success(request, 'Usuário cadastrado com sucesso')
                return lista_empregados(request)
            else:
                messages.error(request, 'Ops.. Tivemos um erro ao tentar cadastrar o funcionário')
                return render(request, 'empregados/new_empregado.html')
        else:
            return render(request, 'empregados/new_empregado.html')
    else:
        return redirect('login')

def delete_empregado(request, emp_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            url = f"https://inm-api-test.herokuapp.com/empregado/deletar/{emp_id}"
            headers = {'content-type': 'application/json'}
            auth = HTTPBasicAuth('inmetrics', 'automacao')
            response = requests.delete(url, headers=headers, auth = auth)
            if response.status_code == 202:
                messages.success(request, 'Funcionário removido com sucesso')
                return lista_empregados(request)
            else:
                messages.error(request, 'Ops.. Não conseguimos remover o funcionário')
                return lista_empregados(request)
    else:
        return redirect('lista_empregados')

def cadastra_empregado(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao):
    url = "https://inm-api-test.herokuapp.com/empregado/cadastrar"
    payload = gera_body(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao)
    headers = {'content-type': 'application/json'}
    auth = HTTPBasicAuth('inmetrics', 'automacao')
    return requests.post(url, data=payload, headers=headers, auth = auth)

def edita_empregado(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao, emp_id):
    url = f"https://inm-api-test.herokuapp.com/empregado/alterar/{emp_id}"
    payload = gera_body(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao)
    headers = {'content-type': 'application/json'}
    auth = HTTPBasicAuth('inmetrics', 'automacao')
    return requests.put(url, data=payload, headers=headers, auth = auth)

def busca_empregado(emp_id):
    url = f"https://inm-api-test.herokuapp.com/empregado/list/{emp_id}"
    response = requests.get(url, auth=HTTPBasicAuth('inmetrics', 'automacao'))
    return response.json()

def gera_body(nome, sexo, cpf, salario, cargo, admissao, tipo_contratacao):
    if sexo == 'Masculino':
          sexo = 'm'
    elif sexo == 'Feminino':
        sexo = 'f'
    else:
        sexo = 'i'

    data = {
            "admissao": admissao,
            "cargo": cargo,
            "comissao": "0,00",
            "cpf": cpf,
            "departamentoId": 1,
            "nome": nome,
            "salario": salario,
            "sexo": sexo,
            "tipoContratacao": tipo_contratacao
            }

    return json.dumps(data)