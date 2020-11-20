from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="sellers_website-index"),
    path('sellers/', views.sellers_home, name="sellers_website-sellers_home"),
    path('sellers/register/', views.sellers_register, name="sellers_website-sellers_register"),
    path('sellers/products/', views.sellers_products, name="sellers_website-sellers_products"),
    path('sellers/product/<product_id>', views.product_visualization, name="sellers_website-product_visualization"),
    path('sellers/product/register/', views.product_register, name="sellers_website-product_register"),
    path('sellers/product/register/success', views.product_success, name="sellers_website-product_register_success"),
    path('add_new_product', views.add_new_product, name="add_new_product"),
    path('add_new_seller', views.add_new_seller, name="add_new_seller"),
    # path('bought/<item_id>', views.bought_item, name="shopping_list-bought"),
    # path('delete_item/', views.delete_item, name="shopping_list-delete"),
    # path('delete_all/', views.delete_all, name="shopping_list-delete_all"),
]
