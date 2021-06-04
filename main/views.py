from django.shortcuts import render

from main.models import Category, Recipe


def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    recipes = Recipe.objects.filter(category_id=slug)
    return render(request, 'category_detail.html', locals())
