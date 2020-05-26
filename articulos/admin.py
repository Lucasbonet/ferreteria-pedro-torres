# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Productos

# Register your models here.
class ProductosAdmin (admin.ModelAdmin):
    list_display=("nombre", "codigo", "precio")
    search_fields=("nombre", "codigo")

admin.site.register(Productos, ProductosAdmin)
