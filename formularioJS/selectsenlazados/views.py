# -*- coding: utf-8 -*-
"""!
Vistas del módulo

@file selectsenlazados/views.py
@author Angelo Osorio
@license Fundación CENDITEL (2018)
@version 1.0 - 2018
"""


from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse

from .models import Poa, Estado, Municipio, Parroquia
from .forms import AgregarPoaForm


## index
# (Consulta y muestra todos los poa, predeterminado como index del módulo)
#
# @param request:           la solicitud de la url de entrar a este método
# @return request:          la solicitud de la url de entrar a este método
# @return index.html:       el template que llenará
# @return context:          Guarda los datos que se mostrarán dentro del context, en una variable
#                           denominada Poas
#
# @author Angelo Osorio
##
def index(request):
    context = {
        'poas': Poa.objects.all().order_by('-id')
    }
    return render(request, 'selectsenlazados/index.html', context)



## add
# (Vista que administrará el formulario de agregar poas)
# 
# @param consulta_estados:      Contiene una consulta con los estados disponibles en la base de datos
# @param consulta_municipios:   Contiene una consulta con los municipios disponibles en la DB
# @param consulta_parroquias:   Contiene una consulta con las parroquias disponibles en la DB
# @param request:               la solicitud de la url de entrar a este método
# @return request:              la solicitud de la url de entrar a este método
# @return index.html:           el template que llenará
# @return context:              Guarda los datos que se mostrarán dentro del context, en una variable
#                               denominada Poas
#
# @author Angelo Osorio
##
def add(request):

    consulta_estados = Estado.objects.all()
    consulta_municipios = Municipio.objects.all()
    consulta_parroquias = Parroquia.objects.all()

    if request.method == "POST":
        form = AgregarPoaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AgregarPoaForm()

    context = {
        'form' : form,
        'estados' : consulta_estados,
        'municipios' : consulta_municipios,
        'parroquias' : consulta_parroquias
    }

    return render(request, 'selectsenlazados/add.html', context)