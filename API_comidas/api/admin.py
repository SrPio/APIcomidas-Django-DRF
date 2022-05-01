from django.contrib import admin

""" from API_comidas.api.models import Plato """
from .models import Plato, Alimento

# Register your models here.
admin.site.register(Plato)
admin.site.register(Alimento)
