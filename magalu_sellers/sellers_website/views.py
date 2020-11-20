from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
# from django.views.generic.base import View
# from .forms import List_Form
# from .models import Shopping_List
# from django.http import HttpResponse
from .forms import Vendedor_Form, Product_Form
from .models import Vendedor, Produto

# Create your views here.

def index(request):
    # my_item = Produto.objects.order_by('id')
    return render(request, 'sellers_website/index.html')

def sellers_home(request):
    return render(request, 'sellers_website/sellers_home.html')

def sellers_register(request):
    return render(request, 'sellers_website/sellers_register.html')

def product_register(request):
    product_form = Product_Form()
    context = {
        # 'my_item': my_item,
        'product_form': product_form
    }
    return render(request, 'sellers_website/product_register.html', context)

def product_success(request):
    return render(request, 'sellers_website/product_success.html')


# class RegisterUserView(View):

#     template_name = 'sellers_website/sellers_register.html'

#     def get(self, request):
#         return render (request, self.template_name)
    
#     def post(self, request):
#         return render(request, self.template_name)


# @require_POST
# def add_new_item(request):
#     form = List_Form(request.POST)

#     if form.is_valid():
#         text = form.cleaned_data.get('text')
#         my_new_item = Shopping_List(item=text)
#         my_new_item.save()

@require_POST
def add_new_product(request):
    product_form = Product_Form(request.POST)


    if product_form.is_valid():
        # print(product_form.cleaned_data['quantidade_produto'])
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

    return redirect('add_new_product')


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