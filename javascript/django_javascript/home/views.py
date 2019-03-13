from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def first(request):
    return render(request, 'home/first.html')


def second(request):
    return render(request, 'home/second.html')