from rest_framework import generics

from apps.public.serializers import *
from apps.public.models import *
# Create your views here.
# /Users/administrator/PycharmProjects/Recipe_Organizer/djangular_rest_seed/apps/public/serializers.py
from djangular_rest_seed.apps.public.models import Ingredient


class RecipeList(generics.ListAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Recipe
    serializer_class = RecipeSerializer


class IngredientList(generics.ListAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    # queryset = Ingredient.objects.all()


class IngredientDetail(generics.CreateAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class AddRecipe(generics.RetrieveUpdateDestroyAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


