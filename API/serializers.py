from rest_framework import serializers

from .models import Recipe, Meal, Staff, Author


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'serve_people_num',
            'get_authors',
            'date',
            'recipe_layout',
            'recipe_intro',
            'prep_time',
            'recipe_ingredients',
            'procedure',
            'get_video_url',
            'get_main_image_url',
            'note',
            'country_origin',
            'nutrition',
            'get_review_avg',
        )


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = (
            'id',
            'title',
            'recipes',
            'get_video_url',
            'get_main_image_url',
            'get_review_avg',
            'category',
        )


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'id',
            'user',
            'is_chiba_staff',
            'section',
            'description',
            'phone',
            'is_curator',
            'is_author',
            'is_chef',
            'staff_id',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'author'
        )
