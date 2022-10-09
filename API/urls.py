from django.urls import path, include
from . import views

app_name = 'API'

urlpatterns = [
    path('featured-recipes/', views.FeaturedRecipeList.as_view()),
    path('recipe/<int:recipe_id>/', views.RecipeDetail.as_view()),
]
