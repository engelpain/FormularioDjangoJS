# -*- coding: utf-8 -*-
"""!
Modelos de datos para un ejemplo de selects anidados en un formulario

@file selectsenlazados/models.py
@author Angelo Osorio
"""

from __future__ import unicode_literals

from django.db import models



class Estado(models.Model):
    """
    Modelo que contiene los nombres de los estados

    @param nombre_estado            Nombre del Estado, type: varchar(250)
    @author                         Angelo Osorio (danielking.321 at gmail.com)
    """
    nombre_estado = models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre_estado



class Municipio(models.Model):
    """
    Modelo que contiene los nombres de los municipios

    @param nombre_municipio         Nombre del Municipio, type: varchar(250)
    @param estado_perteneciente     Estado al que pertenece, type: Clave foránea de Estado
    @author                         Angelo Osorio (danielking.321 at gmail.com)
    """
    nombre_municipio = models.CharField(max_length=250)
    estado_perteneciente = models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.nombre_municipio



class Parroquia(models.Model):
    """
    Modelo que contiene los nombres de las parroquias

    @param nombre_parroquia         Nombre de la Parroquia, type: varchar(250)
    @param municipio_perteneciente  Municipio al que pertenece, type: Clave foránea de Municipio
    @author                         Angelo Osorio (danielking.321 at gmail.com)
    """
    nombre_parroquia = models.CharField(max_length=250)
    municipio_perteneciente = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.nombre_parroquia



class Poa(models.Model):
    """!
    Modelo que contiene los datos del poa
    
    @param nombre                   Nombre del poa, type: varchar(250)
    @param descripcion              Texto del poa, type: text
    @param estado                   Estado del poa, type: Clave foránea de Estado
    @param municipio                Municipio del poa, type: Clave foránea de Municipio
    @param parroquia                Parroquia del poa, type: Clave foránea de Parroquia
    @author                         Angelo Osorio (danielking.321 at gmail.com)
    """
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    def __unicode__(self):
        return "%s de %s" % (self.nombre, self.estado)