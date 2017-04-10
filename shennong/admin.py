from django.contrib import admin

# Register your models here.
from .models import Herb, Recipe, Ingredient


#class HerbAdmin(admin.ModelAdmin):
#    pass


#class IngredientAdmin(admin.ModelAdmin):
#    pass


class IngredientInline(admin.StackedInline):
    """
    """
    
    model = Ingredient
    extra = 1
    #filter_horizontal = ('ingredients',)


class RecipeAdmin(admin.ModelAdmin):
    """
    Allow for recipe ingredients to be added on the admin form.
    """
    
    # TODO: filter_horizontal does not seem to work as expected
    inlines = [IngredientInline]
    #filter_horizontal = ['ingredients',]


admin.site.register(Herb)
#admin.site.register(Herb, HerbAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
#admin.site.register(Ingredient, IngredientAdmin)

