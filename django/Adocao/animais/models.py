from django.db import models

# Create your models here.
#Todas as classes extendem a classes model.Model
class Cidade(models.Model):
    #nome do atributo  = tipo dele e caracteristicas
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, verbose_name="Infome apenas a sigla:")

    # apenas para imprimir o objeto
    def __str__ (self):
        #paranavai (PR)
        return self.nome + "(" + self.estado + ")"

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome Completo')
    email = models.CharField(max_length=50)
    nascimento = models.DateField('Data de Nascimento')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        # faz um cast da data para string
        return self.nome+' - ' + str(self.nascimento)
