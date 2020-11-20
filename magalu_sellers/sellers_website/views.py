from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import Vendedor_Form, Product_Form
from .models import Vendedor, Produto

# Create your views here.

def index(request):
    return render(request, 'sellers_website/index.html')

def sellers_home(request):
    return render(request, 'sellers_website/sellers_home.html')

def sellers_register(request):
    seller_form = Vendedor_Form()
    context = {
        'seller_form': seller_form
    }
    return render(request, 'sellers_website/sellers_register.html', context)

def sellers_products(request):
    my_products = Produto.objects.order_by('id')
    context = {
        'my_products' : my_products
    }
    return render(request, 'sellers_website/sellers_products.html', context)

def product_register(request):
    product_form = Product_Form()
    context = {
        'product_form': product_form
    }
    return render(request, 'sellers_website/product_register.html', context)

def product_success(request):
    return render(request, 'sellers_website/product_success.html')


def product_visualization(request, product_id):
    my_product = Produto.objects.get(pk=product_id)
    context = {
        'my_product' : my_product
    }
    return render(request, 'sellers_website/product_visualization.html', context)

@require_POST
def add_new_product(request):
    product_form = Product_Form(request.POST)

    if product_form.is_valid():
        nome_produto = product_form.cleaned_data['nome_produto']
        marca_produto =  product_form.cleaned_data['marca_produto']
        categoria_produto =  product_form.cleaned_data['categoria_produto']
        preco_produto =  float(product_form.cleaned_data['preco_produto'])
        quantidade_produto =  int(product_form.cleaned_data['quantidade_produto'])
        vendedor =  product_form.cleaned_data['vendedor']
        # imagem_produto =  product_form.cleaned_data.get('imagem_produto')

        new_product = Produto(
            nome_produto=nome_produto,
            marca_produto=marca_produto,
            categoria_produto=categoria_produto,
            preco_produto=preco_produto,
            quantidade_produto=quantidade_produto,
            vendedor=vendedor,
            # imagem_produto=imagem_produto,
            )

        new_product.save()
    else:
        print(product_form.errors)

    return redirect('sellers_website-product_register_success')


@require_POST
def add_new_seller(request):
    seller_form = Vendedor_Form(request.POST,None)


    if seller_form.is_valid():
        nome = seller_form.cleaned_data['nome']
        cpf = seller_form.cleaned_data['cpf']
        email = seller_form.cleaned_data['email']
        telefone = seller_form.cleaned_data['telefone']
        endereco = seller_form.cleaned_data['endereco']
        senha = seller_form.cleaned_data['senha']

        new_seller = Vendedor(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            endereco=endereco,
            senha=senha,
            )

        new_seller.save()
    else:
        print(seller_form.errors)

    return redirect('add_new_seller')

# def bought_item(request, item_id):
#     my_item = Produto.objects.get(pk=item_id)
#     my_item.complete = True
#     my_item.save()

#     return redirect('sellers_website-index')

# def delete_item(request):
#     Produto.objects.filter(complete__exact=True).delete()

#     return redirect('sellers_website-index')

# def delete_all(request):
#     Produto.objects.all().delete()
    
#     return redirect('sellers_website-index')