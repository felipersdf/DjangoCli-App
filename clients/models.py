from django.db import models

# Create your models here.

class Client (models.Model):
    nome = models.CharField(max_length=40, unique=True)    
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=20)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=15)
    país = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nome