from django.contrib import admin
from .models import Produto, Vendedor


# Register your models here.

admin.site.register(Vendedor)
admin.site.register(Produto)