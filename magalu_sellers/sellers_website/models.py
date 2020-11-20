from django.db import models
from django.contrib.auth.models import User
 #Create your models here.

class Vendedor(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    marca_produto = models.CharField(max_length=100)
    categoria_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField()
    quantidade_produto = models.FloatField()
    imagem_produto = models.FileField()
    vendedor = models.ForeignKey(Vendedor, null=True, on_delete=models.SET_NULL)
    #define se o produto pode ser comprado
    #quando False o produto esta disponivel, quando true ele nao esta
    complete = models.BooleanField(default=False) 

    def __str__(self):
        return self.nome_produto



