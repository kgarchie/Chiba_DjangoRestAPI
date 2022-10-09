import random

from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.
meal_category_choices = ['l', 'vn', 'vr', 'b', 'm']
recipe_layouts = ['a', 'm', 'd']


class FeaturedRecipeList(APIView):
    def get_featured(self):
        val = Recipe.objects.filter(featured=True).distinct()
        return val

    def get(self, request, format=None):
        featured_recipes = self.get_featured()
        serializer = RecipeSerializer(featured_recipes, many=True)
        return Response(serializer.data)


class RecipeDetail(APIView):
    def get_recipe(self, recipe_id):
        try:
            return Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, recipe_id, format=None):
        recipe = self.get_recipe(recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
