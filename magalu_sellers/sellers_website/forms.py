from django import forms
from sellers_website.models import Vendedor, Produto


class Vendedor_Form(forms.Form):
    nome = forms.CharField(max_length=200)
    cpf = forms.CharField(max_length=14)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=11)
    endereco = forms.CharField(max_length=200)
    senha = forms.CharField(max_length=12)
    class Meta:
        model = Vendedor

class Product_Form(forms.Form):
    # text = forms.CharField(max_length=100,
    # widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Insira um produto'
    #     }
    #  ))
    nome_produto = forms.CharField(max_length=100,
       widget=forms.TextInput(
        attrs={
            'placeholder': 'ex.: Aspirador de Pó'
        })
    )
    marca_produto = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex.: LG'
        }))
    categoria_produto = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex.: Eletronico'
            })
    )
    preco_produto = forms.FloatField()
    quantidade_produto = forms.IntegerField()
    # imagem_produto = forms.FileField()
    vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.all())
    
    class Meta:
        model = Produto

