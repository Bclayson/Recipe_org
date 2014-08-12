from django.conf.urls import patterns, include, url
from apps.public.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('apps.public.views',

    # Examples:
    # url(r'^$', 'djangular_rest_seed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^recipes$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^recipe-add$', AddRecipe.as_view(), name='add-recipe'),

    url(r'^ingredients$', IngredientList.as_view(), name='ingredient-list'),
    url(r'^ingredients/(?P<pk>[0-9]+)$', IngredientDetail.as_view(), name='ingredient-detail'),




)
