from django.contrib import admin

# Register your models here.
from .models import Herb, Recipe, Ingredient


admin.site.register(Herb)
admin.site.register(Recipe)
admin.site.register(Ingredient)

