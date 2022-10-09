from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class MealLayouts(models.TextChoices):
    APPETIZER = 'a', _('APPETIZER')
    MAIN = 'm', _('MAIN')
    DESSERT = 'd', _('DESSERT')


class MealTimes(models.TextChoices):
    BREAKFAST = 'bf', _('Breakfast')
    LUNCH = 'l', _('Lunch')
    SUPPER = 's', _('Supper')
    ANY = 'a', _('Any Time')


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_chiba_staff = models.BooleanField(default=False)
    section = models.CharField(max_length=15, default="General")
    description = models.TextField(default="General")
    phone = models.CharField(max_length=15)

    is_curator = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    is_chef = models.BooleanField(default=False)

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
    prep_time = models.IntegerField(default=0.5)
    recipe_ingredients = models.TextField()  # remember to parse ingredients use delimiters
    procedure = models.TextField()
    video_tutorial = models.FileField()
    note = models.TextField()
    country_origin = models.CharField(max_length=20)
    nutrition = models.TextField()

    def __str__(self):
        return self.title


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    star = models.IntegerField()  # remember to validate input to be less than 5
    note = models.TextField()
    created = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['created']

    def __str__(self):
        return str(self.user.username) + "'s review"


class Meals(models.Model):
    title = models.CharField(max_length=50)
    serve_time = models.CharField(choices=MealTimes.choices, default=MealTimes.ANY, max_length=10)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.title
