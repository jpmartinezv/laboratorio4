from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from cashier.models import Cashier

class CashierForm(ModelForm):
    class Meta:
        model = Cashier
        fields = ['attendant', 'store', 'address']

def cashier_list(request, template_name='cashier/cashier_list.html'):
    cashier = Cashier.objects.all()
    data = {'object_list': cashier}
    return render(request, template_name, data)

def cashier_create(request, template_name='cashier/cashier_form.html'):
    form = CashierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cashier:cashier_list')
    return render(request, template_name, {'form': form})

def cashier_update(request, pk, template_name='cashier/cashier_form.html'):
    cashier = get_object_or_404(Cashier, pk=pk)
    form = CashierForm(request.POST or None, instance=cashier)
    if form.is_valid():
        form.save()
        return redirect('cashier:cashier_list')
    return render(request, template_name, {'form': form})

def cashier_delete(request, pk, template_name='cashier/cashier_confirm_delete.html'):
    cashier = get_object_or_404(Cashier, pk=pk)
    if request.method == 'POST':
        cashier.delete()
        return redirect('cashier:cashier_list')
    return render(request, template_name, {'objects': cashier})
