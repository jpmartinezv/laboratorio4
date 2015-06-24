from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from account.models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['idClient', 'status']

def account_list(request, template_name='account/account_list.html'):
    account = Account.objects.all()
    data = {'object_list': account}
    return render(request, template_name, data)

def account_create(request, template_name = 'account/account_form.html'):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('account:account_list')
    return render(request, template_name, {'form' : form})

def account_update(request, pk, template_name='account/account_form.html'):
    account = get_object_or_404(Account, pk=pk)
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save()
        return redirect('account:account_list')
    return render(request, template_name, {'form' : form})

def account_delete(request, pk, template_name='account/account_confirm_delete.html'):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account:account_list')
    return render(request, template_name, {'objects': account})
