from django.shortcuts import render
from clube42.cpr.forms import DespesaForm


def listadespesas(request):

    contexto = {'despesa': DespesaForm()}
    return render(request, 'despesas/despesa.html', contexto)
