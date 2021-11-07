from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse # To generate URLs by reversing URL patterns

from recipes.apps.accounts.models import CustomUser


class Ingredient(models.Model):
    """This object represents an ingredient of a recipe."""
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

class IngredientList(models.Model):
    """This object represents the quantity of ingredient needed in a recipe"""
    UNITY = (
        ("g", "gramme"),
        ("mg", "milligramme"),
        ("l", "litre"), 
        ("ml", "millilitre"),
        ("kg", "kilogramme"),
        ("nb", "nombre"),
        ("cc", "cuillère à café"),
        ("v", "verre (petit)"),
    )
    recipe =  models.ForeignKey('Recipe', on_delete=models.CASCADE, null=False, blank=False)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    unity = models.CharField(max_length=10, choices=UNITY)

    def __str__(self):
        return f'{self.recipe.title} - {self.quantity} {self.unity} {self.ingredient.name}'
    

class Recipe(models.Model):
    """This object represents the recipe with the meta  data"""

    DRAFT = "D"
    HIDDEN = "H"
    PUBLISHED = "P"
    ENTRY_STATUS = (
        (DRAFT, _("Draft")),
        (HIDDEN, _("Hidden")),
        (PUBLISHED, _("Published")),
    )

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000, null=True, blank=True)
    status = models.CharField(max_length=10, choices=ENTRY_STATUS)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")

    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Return the url to access to a particular recipe."""
        return reverse('recipe-detail', args=[str(self.id)])