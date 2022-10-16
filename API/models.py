import random

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg
from django.utils.text import slugify

host_url = 'https://bosireallan.pythonanywhere.com'  # should make as environment variable


# host_url = 'http://127.0.0.1:8000'


# Create your models here.

class MealLayouts(models.TextChoices):
    APPETIZER = 'a', _('APPETIZER')
    MAIN = 'm', _('MAIN')
    DESSERT = 'd', _('DESSERT')


class MealTimes(models.TextChoices):
    BREAKFAST = 'b', _('Breakfast')
    LUNCH = 'l', _('Lunch')
    SUPPER = 's', _('Supper')
    ANY = 'a', _('Any Time')


class MealCategories(models.TextChoices):
    LEAN = 'l', _('Lean - (Low Calories)')
    VEGAN = 'vn', _('Vegan')
    VEGETARIAN = 'vr', _('Vegetarian')
    BALANCED = 'b', _('Balanced')
    MUSCLE = 'm', _('Work Out')


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author.username)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.author.username


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_chiba_staff = models.BooleanField(default=False)
    section = models.CharField(max_length=15, default="General")
    description = models.TextField(default="General")
    phone = models.CharField(max_length=15, blank=True, null=True)

    is_curator = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    is_chef = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Staff, self).save(*args, **kwargs)

    @property
    def staff_id(self):
        return str(self.section)[0:3].capitalize() + str(self.description)[0:3].capitalize() + str(self.user.id)

    def __str__(self):
        return "Staff " + str(self.user.username)


class Recipe(models.Model):
    title = models.CharField(max_length=25)
    serve_people_num = models.IntegerField()
    author = models.ManyToManyField(Author)
    date = models.DateTimeField(auto_now_add=True)
    recipe_layout = models.TextField(max_length=10, choices=MealLayouts.choices, default=MealLayouts.MAIN)
    recipe_intro = models.TextField()
    prep_time = models.IntegerField(default=1)
    recipe_ingredients = models.TextField()  # remember to parse ingredients use delimiters
    procedure = models.TextField()
    video_tutorial = models.FileField(upload_to='videos', blank=True, null=True)
    main_image = models.FileField(
        upload_to='images', blank=True,
        null=True)  # to fix the images issue require at least one image after every 2 steps
    note = models.TextField()
    country_origin = models.CharField(max_length=20)
    nutrition = models.TextField()
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def get_review_avg(self):
        reviews = RecipeReviews.objects.filter(recipe_id=self.id)
        avg_star = reviews.aggregate(Avg('star'))

        return avg_star

    @property
    def get_video_url(self):
        return f'{host_url}{self.video_tutorial.url}'

    @property
    def get_main_image_url(self):
        return f'{host_url}{self.main_image.url}'

    @property
    def get_authors(self):
        authors = []
        slugs = []
        for item in self.author.all():
            authors.append(item.author)
            slugs.append(item.slug)

        staggered_authors = {
            "names": [item.username for item in authors],
            "slugs": [item for item in slugs],
        }
        return staggered_authors


class RecipeReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    star = models.IntegerField()  # remember to validate input to be less than 5
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    valid_review = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(RecipeReviews, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Recipe Reviews'
        ordering = ['created']

    def __str__(self):
        return str(self.user.username) + "'s Recipe Review"


class Meal(models.Model):
    title = models.CharField(max_length=50)
    serve_time = models.CharField(choices=MealTimes.choices, default=MealTimes.ANY, max_length=10)
    recipes = models.ManyToManyField(Recipe)
    featured = models.BooleanField()
    video = models.FileField(upload_to='videos', blank=True, null=True)
    main_image = models.FileField(upload_to='images', blank=True, null=True)
    category = models.CharField(max_length=15, default=MealCategories.BALANCED, choices=MealCategories.choices)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Meal, self).save(*args, **kwargs)

    @property
    def get_review_avg(self):
        reviews = MealReviews.objects.filter(meal_id=self.id).all()
        avg_star = reviews.aggregate(Avg('star'))

        return avg_star

    @property
    def get_video_url(self):
        return f'{host_url}{self.video.url}'

    @property
    def get_main_image_url(self):
        return f'{host_url}{self.main_image.url}'

    def __str__(self):
        return self.title


class MealReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    star = models.IntegerField()  # remember to validate input to be less than 5
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    valid_review = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(MealReviews, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Meal Reviews'

    def __str__(self):
        return str(self.user.username) + "'s Meal Review"
