from django.shortcuts import render, redirect
from .models import Cliente, Venda
from .forms import ClienteForm, VendaForm
from django.db.models import Q
from datetime import datetime

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/clientes.html', {'clientes': clientes})



def novo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/form_cliente.html', {'form': form})




def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'core/form_cliente.html', {'form': form})



def deletar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista_clientes')



def lista_vendas(request):
    cliente_id = request.GET.get('cliente')
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')
    vendas = Venda.objects.all()



    if cliente_id:
        vendas = vendas.filter(cliente__id=cliente_id)
    if data_inicio:
        vendas = vendas.filter(data_venda__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data_venda__lte=data_fim)

    return render(request, 'core/vendas.html', {'vendas': vendas})



def nova_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_vendas')
    return render(request, 'core/form_venda.html', {'form': form})
