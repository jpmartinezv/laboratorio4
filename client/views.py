from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from client.models import Client
from account.models import Account

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['firstName', 'lastName', 'dni', 'address', 'phone', 'email']

def client_list(request, template_name='client/client_list.html'):
    client = Client.objects.all()
    data = {'object_list': client}
    return render(request, template_name, data)

def client_create(request, template_name='client/client_form.html'):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client:client_list')
    return render(request, template_name, {'form': form})

def client_update(request, pk, template_name='client/client_form.html'):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client:client_list')
    return render(request, template_name, {'form': form})

def client_delete(request, pk, template_name='client/client_confirm_delete.html'):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client:client_list')
    return render(request, template_name, {'objects': client})

def client_profile(request, pk, template_name='client/client_profile.html'):
    client = get_object_or_404(Client, pk=pk)
    accounts = Account.objects.filter(client=pk).values()
    data = {'client': client, 'accounts': accounts}
    return render(request, template_name, data)
