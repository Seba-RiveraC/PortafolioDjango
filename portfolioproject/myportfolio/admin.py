# admin.py
from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)
