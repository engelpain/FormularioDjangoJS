# -*- coding: utf-8 -*-
"""!
Clase para administrar los atributos de los inputs en el formulario respectivo

@file selectsenlazados/forms.py
@author Angelo Osorio
@license Fundación CENDITEL (2018)
@version 1.0 - 2018
"""

from django import forms
from .models import Poa


class AgregarPoaForm(forms.ModelForm):
    """
    Modelo de formulario para el formulario de agregar POA

    @author                         Angelo Osorio (danielking.321 at gmail.com)
    """
    class Meta:
        model = Poa
        fields = ('nombre', 'descripcion', 'estado', 'municipio', 'parroquia')