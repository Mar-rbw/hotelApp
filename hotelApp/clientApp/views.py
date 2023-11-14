from django.shortcuts import render, redirect
from clientApp.models import Client
from clientApp.forms import ClientForm
# Create your views here.

def listaClient(request):
    clientes = Client.objects.all()
    return render(request, 'clientApp/listaClient.html', {'clientApp':clientes})

def crearClient(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listClient')
    return render(request, 'clientApp/crearClient.html', {'form':form})

def editarClient(request, id):
    client = Client.object.get(id=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listaClient')
    return render(request, 'clientApp/editarClient.html', {'form':form, 'clint': client})

def eliminarClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('listaClient')