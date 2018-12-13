from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')

def store(request, stores_id):
    store = Pizza.objects.get(id=stores_id)
    entries = stores.entry_set.order_by('-date_added')
    context = {'store': store, 'prilavok': prilavok}
    return render(request, 'pizzas/store.html', context)
