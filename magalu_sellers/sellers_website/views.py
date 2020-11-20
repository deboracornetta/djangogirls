from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .forms import List_Form
from .models import Produto


# Create your views here.

def index(request):
    my_item = Produto.objects.order_by('id')
    form = List_Form()
    context = {
        'my_item': my_item,
        'form': form
    }
    return render(request, 'sellers_website/index.html', context)

def sellers_register(request):
    return render(request, 'sellers_website/sellers_register.html')

@require_POST
def add_new_item(request):
    form = List_Form(request.POST)

    if form.is_valid():
        text = form.cleaned_data.get('text')
        my_new_item = Produto(nome_produto=text)
        my_new_item.save()

    return redirect('sellers_website-index')


def bought_item(request, item_id):
    my_item = Produto.objects.get(pk=item_id)
    my_item.complete = True
    my_item.save()

    return redirect('sellers_website-index')

def delete_item(request):
    Produto.objects.filter(complete__exact=True).delete()

    return redirect('sellers_website-index')

def delete_all(request):
    Produto.objects.all().delete()
    
    return redirect('sellers_website-index')