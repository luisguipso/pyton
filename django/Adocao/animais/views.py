# Uma classe simples para exibir uma página simples
from django.views.generic import TemplateView
# Serve para páginas que só tem HTML e talvez alguma consulta
# para listar coisas do banco

#importar modelos
from .models import *

#importar os metodos View para inserir, alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#importar a função para gerar o endereço de nossas urls inteiras
from django.urls import reverse_lazy

# Página inicial
class Index(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "pagina_inicial.html" # deve estar na pasta templates


# Página de ajuda
class Ajuda(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "ajuda.html" # deve estar na pasta templates

class Contato(TemplateView):
    template_name = 'contato.html'

class Sobre(TemplateView):
    template_name = 'sobre.html'

class Procurar(TemplateView):
    template_name = 'procurar.html'

class CidadeCreate(CreateView):
    # indentificar o modelo
    model = Cidade
    #define pra onde vai redirecionar quando inserir
    success_url = reverse_lazy('index')
    #define qual o template vai seu usado
    template_name = 'form.html'
    #define quais campos vao estar no formulario
    fields = ['nome', 'estado']

class CidadeUpdate(UpdateView):
    model = Cidade
    success_url = reverse_lazy('index')
    template_name = 'form.html'
    fields = ['nome', 'estado']


class CidadeDelete(DeleteView):
    model = Cidade
    success_url = reverse_lazy('index')
    template_name = 'form_delete.html'


class PessoaCreate(CreateView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'form.html'
    fields = ['nome','email','nascimento', 'cidade']



class PessoaUpdate(UpdateView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'form.html'
    fields = ['nome', 'email', 'nascimento', 'cidade']

class PessoaDelete(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'form_delete.html'
