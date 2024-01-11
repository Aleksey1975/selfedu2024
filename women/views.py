from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, cat_id):
    return HttpResponse(f"Статьи по категориям, {cat_id}")

def archive(request, year):
    return HttpResponse(f"Статьи по году: {year}")