from django.contrib import admin

# Register your models here.
from .models import Herb, Recipe, Ingredient


class HerbAdmin(admin.ModelAdmin):
    """
    Tailor the list display of herb items on the admin form.
    """
    
    list_display = ('chinese', 'pinyin', 'latin', 'english')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'herb')


class IngredientInline(admin.StackedInline):
    """
    """
    
    model = Ingredient
    extra = 1
    #filter_horizontal = ('ingredients',)


class RecipeAdmin(admin.ModelAdmin):
    """
    Allow for recipe ingredients to be added on the admin form.
    Tailor the list display of recipe information on the admin form.
    """
    
    list_display = ('chinese', 'pinyin', 'english')
    
    # TODO: filter_horizontal does not seem to work as expected
    inlines = [IngredientInline]
    #filter_horizontal = ['ingredients',]


admin.site.register(Herb, HerbAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

