from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.RecipeListView.as_view(), name='recipes'),
    path('myrecipes/', views.RecipeByUserListView.as_view(), name='my-recipes'),
    path('<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]
