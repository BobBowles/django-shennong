from django.contrib import admin

# Register your models here.
from .models import Herb, Recipe, Ingredient


class HerbAdmin(admin.ModelAdmin):
    """
    Tailor the list display of herbs on the admin form.
    Configure a search engine.
    """
    
    list_display = ('chinese', 'pinyin', 'latin', 'english')
    search_fields = ['chinese', 'pinyin', 'latin', 'english']


class IngredientAdmin(admin.ModelAdmin):
    """
    Tailor the list display of ingredients on the admin form.
    Configure a search engine.
    """
    
    list_display = ('recipe', 'herb')
    search_fields = [
        'recipe__chinese', 
        'recipe__pinyin', 
        'recipe__english', 
        'herb__chinese',
        'herb__pinyin',
        'herb__latin',
        'herb__english',
        ]


class IngredientInline(admin.StackedInline):
    """
    """
    
    model = Ingredient
    extra = 1
    #filter_horizontal = ('ingredients',)


class RecipeAdmin(admin.ModelAdmin):
    """
    Allow for recipe ingredients to be added on the admin form.
    Tailor the list display of recipes on the admin form.
    Configure a search engine.
    """
    
    list_display = ('chinese', 'pinyin', 'english')
    search_fields = ['chinese', 'pinyin', 'english']
    
    # TODO: filter_horizontal does not seem to work as expected
    inlines = [IngredientInline]
    #filter_horizontal = ['ingredients',]


admin.site.register(Herb, HerbAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

