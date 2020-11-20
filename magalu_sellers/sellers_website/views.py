from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import Vendedor_Form, Product_Form, Product_Update
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
    product_form = Product_Update(request.POST or None, instance=my_product)

    context = {
        'product_form' : product_form,
        'my_product' : my_product
    }
    return render(request, 'sellers_website/product_visualization.html', context)

@require_POST
def add_new_product(request):
    product_form = Product_Form(request.POST)

    if product_form.is_valid():
        
        product_form.save()
    else:
        print(product_form.errors)

    return redirect('sellers_website-product_register_success')

def update_product(request, id):
    instance = Produto.objects.get(pk=id)
    product_form = Product_Update(request.POST or None, instance=instance)

    if product_form.is_valid():
        product_form.save()
    else:
        print(product_form.errors)

    return redirect('sellers_website-product_register_success')

@require_POST
def add_new_seller(request):
    seller_form = Vendedor_Form(request.POST)

    if seller_form.is_valid():
        seller_form.save()
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