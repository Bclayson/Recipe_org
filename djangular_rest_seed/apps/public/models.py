from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="Tell us about this Mancipe")
    prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50, default="in minutes")
    ingredients = models.ManyToManyField('Ingredient', null=True, blank=True)
    instructions = models.TextField(default="How do we make this?")
    image = models.CharField(max_length=100, default="image here")



    def __unicode__(self):
        return self.name
# Create your models here.


ingredient_category = (
    ('NONE', 'Category'),
    ('MEAT', 'Meat'),
    ('VEGETABLES', 'Not Meat, Vegetables'),
    ('FRUIT', 'Not Meat, Fruit'),
    ('OTHER', "Not Meat...other"),
    ('ALSO NOT MEAT', 'Also Not Meat (Spices or condiments)'),
)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=ingredient_category, default="Category")



    def __unicode__(self):
        return self.name





    class Meta:
        verbose_name_plural = "Ingredient categories"

    def __unicode__(self):
        return self.name


