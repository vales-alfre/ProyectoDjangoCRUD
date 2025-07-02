from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item creado correctamente')
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form, 'title': 'Registrar Item'})


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item actualizado correctamente')
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form, 'title': 'Editar Item'})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item eliminado correctamente')
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'item': item})
