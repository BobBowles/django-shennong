from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, Herb


def index(request):
    """
    Display a list of recipes to select from.
    """
    recipe_index = Recipe.objects.order_by('pinyin')
#    template = loader.get_template('shennong/index.html')
    context = {
        'recipe_index': recipe_index,
    }
#    return HttpResponse(template.render(context, request))
    return render(request, 'shennong/index.html', context)


def recipe_header(request, id):
    """
    Display header data for a recipe.
    """
    recipe = get_object_or_404(Recipe, pk=id)
    
    return render(request, 'shennong/recipe_header.html', {'recipe': recipe,})




def recipe_full(request, id):
    """
    Display full data for a recipe.
    """
    recipe = get_object_or_404(Recipe, pk=id)
    
    return render(request, 'shennong/recipe_full.html', {'recipe': recipe,})


def herb(request, id):
    """
    Display data for an herb.
    """
    herb = get_object_or_404(Herb, pk=id)
    
    return render(request, 'shennong/herb.html', {'herb': herb,})

