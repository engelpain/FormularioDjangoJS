# -*- coding: utf-8 -*-
"""!
Clases para otorgar acceso a los modelos de la aplicación selectsenlazados al administrador de
Django

@file selectsenlazados/admin.py
@author Angelo Osorio
@license Fundación CENDITEL (2018)
@version 1.0 - 2018
"""
from __future__ import unicode_literals

from django.contrib import admin

from .models import Poa, Estado, Municipio, Parroquia
 
class PoaAdmin(admin.ModelAdmin):
  ordering = ('-id',)
  search_fields = ('nombre', 'descripcion',)
 
admin.site.register(Poa, PoaAdmin)

class EstadoAdmin(admin.ModelAdmin):
  ordering = ('-id',)

admin.site.register(Estado, EstadoAdmin)

class MunicipioAdmin(admin.ModelAdmin):
  ordering = ('-id',)

admin.site.register(Municipio, MunicipioAdmin)

class ParroquiaAdmin(admin.ModelAdmin):
  ordering = ('-id',)

admin.site.register(Parroquia, ParroquiaAdmin)