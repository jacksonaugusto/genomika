# -*- coding: utf-8 -*-
from django.shortcuts import render



# Create your views here.

def home(request):
    tela1 = 'telas/index.html'
    return render(request, tela1)


def resultado(request):
    tela2 = 'telas/resultado.html'
    return render(request,tela2)





