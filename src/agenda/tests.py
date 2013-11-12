"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

# -*- encoding: utf-8 -*-

from django.shortcuts import render

from agenda.models import ItemAgenda

def index(request):
    lista_itens = ItemAgenda.objects.all()
    return render(request, "lista.html",
                  {'lista_itens': lista_itens})

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
