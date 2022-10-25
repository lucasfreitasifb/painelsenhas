# experiencein/perfis/views.py 
from django.shortcuts import render 
from senhas.models import Senha


def index(request): 
    return render(request, 'index.html', {'senhas' : Senha.objects.all()})

def exibir(request, id_senha):
    print("Id Senha: {}".format(id_senha))
    senha = Senha.objects.get(id_senha=id_senha)

    return render(request, 'senha.html', { "senha" : senha})


def chamar(request, id_senha_chamada):
    senha_a_chamar = Senha.objects.get(id_senha=id_senha_chamada)
    senha_a_chamar.chamar(id_senha_chamada)
    return render(request, 'index.html', {'senhas' : Senha.objects.all()})