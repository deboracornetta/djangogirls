from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="sellers_website-index"),
    path('sellers/register/', views.sellers_register, name="sellers_website-sellers_register"),
    # path('add/', views.add_new_item, name="shopping_list-add"),
    # path('bought/<item_id>', views.bought_item, name="shopping_list-bought"),
    # path('delete_item/', views.delete_item, name="shopping_list-delete"),
    # path('delete_all/', views.delete_all, name="shopping_list-delete_all"),
]
