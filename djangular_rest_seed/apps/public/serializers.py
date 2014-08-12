from models import *
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient



class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe



