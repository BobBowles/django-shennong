from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Recipe, Herb


def index(request):
    recipe_index = Recipe.objects.order_by('pinyin')
    output = ', '.join([recipe.pinyin for recipe in recipe_index])
    return HttpResponse(output)


def recipe_header(request, id):
    response = "Header Description of Recipe {}."
    return HttpResponse(response.format(id))


def recipe_full(request, id):
    response = "Full Description of Recipe {}."
    return HttpResponse(response.format(id))


def herb(request, id):
    response = "Description of Herb {}."
    return HttpResponse(response.format(id))

