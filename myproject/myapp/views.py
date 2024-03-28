from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    with open('myapp/templates/1.html', 'r', encoding='utf-8') as file:
        first_page = file.read()
    return HttpResponse(first_page)


def index(request):
    with open('myapp/templates/index.html', 'r', encoding='utf-8') as file:
        index = file.read()
    return HttpResponse(index)


def about(request):
    with open('myapp/templates/about.html', 'r', encoding='utf-8') as file:
        about = file.read()
    return HttpResponse(about)
