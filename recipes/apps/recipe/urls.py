from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.RecipeListView.as_view(), name='recipes'),
    path('myrecipes/', views.RecipeByUserListView.as_view(), name='my-recipes'),
    path('<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
]
