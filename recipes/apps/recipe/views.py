from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
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


class RecipeListView(PermissionRequiredMixin, generic.ListView):
    model = Recipe
    paginate_by = 1
    permission_required = 'recipe.view_recipe'

    #context_object_name = 'recipe_list' # this is a default name givent by django
    # If you want to use filter and limit the result to only 5 elements
    #queryset = Recipe.object.filter(title_icontains='gateau')[:5] 
    # to use a different template file than /application_name/templates/application_name/the_model_name_list.html
    #template_name = 'recipe/my_arbitrary_template_name.html

class RecipeByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing recipe written by the current user."""
    model = Recipe
    template_name = 'recipe/recipe_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Recipe.objects.filter(created_by=self.request.user).order_by('-last_update')

class RecipeDetailView(generic.DetailView):
    model = Recipe


## Forms
class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'content', 'status']
    #exclude = ['last_update', 'creation_date', 'edited_by', 'created_by']
    initial = {'status': 'Draft'}

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'content']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')
