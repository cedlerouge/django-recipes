from django.shortcuts import render
from django.views import generic
from recipes.apps.recipe.models import Ingredient, IngredientList, Recipe

def index(request):
    """View function for home page of the site"""

    # Generate counts of some of the main objects
    num_recipes = Recipe.objects.all().count()

    context = {
        'num_recipes': num_recipes,
    }

    # Render the HTML template index.html aith the data in the context variable
    return render(request, 'index.html', context=context)


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 1

    #context_object_name = 'recipe_list' # this is a default name givent by django
    # If you want to use filter and limit the result to only 5 elements
    #queryset = Recipe.object.filter(title_icontains='gateau')[:5] 
    # to use a different template file than /application_name/templates/application_name/the_model_name_list.html
    #template_name = 'recipe/my_arbitrary_template_name.html

class RecipeDetailView(generic.DetailView):
    model = Recipe