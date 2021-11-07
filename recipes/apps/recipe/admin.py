from django.contrib import admin
from django.db.models import fields

from recipes.apps.recipe.models import Ingredient, IngredientList, Recipe

admin.site.register(Ingredient)
#admin.site.register(IngredientList)
#admin.site.register(Recipe)

# Change the presentation of the class IngredientList in admin panel
class IngredientListAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity', 'unity')
    list_filter = ('recipe', 'ingredient')

class IngredientListInline(admin.TabularInline):
    model = IngredientList
    extra = 0

admin.site.register(IngredientList, IngredientListAdmin)

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'status', 'created_by', 'edited_by')
        }),
        ('Description', {
            'fields': ('content',)
        }),
    )
    inlines = [IngredientListInline]
admin.site.register(Recipe, RecipeAdmin)