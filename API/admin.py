from django.contrib import admin
from .models import Author, Recipe, Staff, RecipeReviews, MealReviews, Meal

# Register your models here.

admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Staff)
admin.site.register(RecipeReviews)
admin.site.register(MealReviews)
admin.site.register(Meal)

