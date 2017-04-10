from django.db import models

# Create your models here.


class Herb(models.Model):
    """
    A herb describes a plant from the canon of Chinese herbs. It provides
    the herb's Chinese name, the name in Pinyin, the Latin name, and common 
    English name.
    """
    
    chinese = models.CharField(max_length=20)
    pinyin = models.CharField(max_length=50)
    latin = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    
    def __str__(self):
        return self.pinyin


class Recipe(models.Model):
    """
    A recipe includes the list of herbs to use for a particular treatment. The 
    recipe has a Chinese name, a Pinyin name, and an English description.
    """
    
    chinese = models.CharField(max_length=20)
    pinyin = models.CharField(max_length=50)
    english = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Herb, through='Ingredient')
    
    def __str__(self):
        return self.pinyin


class Ingredient(models.Model):
    """
    An ingredient cross-references herbs and recipes.
    TODO: may include details of proportions/amounts of a herb in a recipe.
    """
    
    recipe = models.ForeignKey(Recipe)
    herb = models.ForeignKey(Herb)
    
    def __str__(self):
        return '{0} contains {1}'.format(self.recipe, self.herb)
