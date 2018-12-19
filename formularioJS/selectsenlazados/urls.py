# -*- coding: utf-8 -*-
"""!
Array que direcciona las urls del navegador a las vistas

@file selectsenlazados/urls.py
@author Angelo Osorio
@license Fundación CENDITEL (2018)
@version 1.0 - 2018
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='agregarPoa'),
]