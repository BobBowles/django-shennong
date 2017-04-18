from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Recipe, Herb

# Used for search query.
import re
from django.db.models import Q


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """
    Splits the query string in invidual keywords, getting rid of unecessary
    spaces and grouping quoted words together.

    Example:
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    """
    Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.
    """
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def index(request):
    """
    Display a list of recipes to select from.
    The list can be narrowed down using a search bar.
    """
    recipe_index = None
    recipe_search_terms = ""

    if ((request.method == "GET") and
        ('query' in request.GET) and
        request.GET['query'].strip()
        ):
        recipe_search_terms = request.GET['query']
        recipe_query = get_query(
            recipe_search_terms, ['chinese', 'pinyin', 'english',])
        recipe_index = Recipe.objects.filter(recipe_query).order_by('pinyin')
    else:
        recipe_index = Recipe.objects.order_by('pinyin')

    context = {
        'recipe_index': recipe_index,
        'recipe_search_terms': recipe_search_terms,
    }
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
