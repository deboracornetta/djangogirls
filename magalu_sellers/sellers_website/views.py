from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic.base import View
# from .forms import List_Form
# from .models import Shopping_List

# Create your views here.

def index(request):
    # my_item = Shopping_List.objects.order_by('id')
    # form = List_Form()
    # context = {
    #     'my_item' : my_item,
    #     'form' : form
    # }
    return render(request, 'sellers_website/index.html')

def sellers_home(request):
    return render(request, 'sellers_website/sellers_home.html')

def sellers_register(request):
    return render(request, 'sellers_website/sellers_register.html')

def product_register(request):
    return render(request, 'sellers_website/product_register.html')

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

#     return redirect('shopping_list-index')


# def bought_item(request, item_id):
#     my_item = Shopping_List.objects.get(pk=item_id)
#     my_item.complete = True
#     my_item.save()

#     return redirect('shopping_list-index')


# def delete_item(request):
#     Shopping_List.objects.filter(complete__exact=True).delete()

#     return redirect('shopping_list-index')

# def delete_all(request):
#     Shopping_List.objects.all().delete()
    
#     return redirect('shopping_list-index')