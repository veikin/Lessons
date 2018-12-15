from django.shortcuts import render
from .models import Pizza


def index(request):
    return render(request, 'pizzas/index.html')


def store(request, toppings_id):
    store = Pizza.objects.get(id=_id)
    toppings = store.entry_set.order_by('-date_added')
    context = {'store': store, 'toppings': toppings}
    return render(request, 'pizzas/store.html', context)
