from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from transaction.models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'date', 'type', 'amount', 'destination']

def transaction_list(request, template_name='transaction/transaction_list.html'):
    transaction = Transaction.objects.all()
    data = {'object_list': transaction}
    return render(request, template_name, data)

def transaction_create(request, template_name='transaction/transaction_form.html'):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('transaction:transaction_list')
    return render(request, template_name, {'form': form})

def transaction_update(request, pk, template_name='transaction/transaction_form.html'):
    transaction = get_object_or_404(Transaction, pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('transaction:transaction_list')
    return render(request, template_name, {'form': form})

def transaction_delete(request, pk, template_name='transaction/transaction_confirm_delete.html'):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction:transaction_list')
    return render(request, template_name, {'objects': transaction})
