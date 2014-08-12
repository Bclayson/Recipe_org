# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.measurement'
        db.delete_column(u'public_recipe', 'measurement')

        # Deleting field 'IngredientCategory.name'
        db.delete_column(u'public_ingredientcategory', 'name')

        # Adding field 'IngredientCategory.categories'
        db.add_column(u'public_ingredientcategory', 'categories',
                      self.gf('django.db.models.fields.CharField')(default='Meat', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Recipe.measurement'
        db.add_column(u'public_recipe', 'measurement',
                      self.gf('django.db.models.fields.CharField')(default='Make it a manly serving', max_length=20),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'IngredientCategory.name'
        raise RuntimeError("Cannot reverse this migration. 'IngredientCategory.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'IngredientCategory.name'
        db.add_column(u'public_ingredientcategory', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'IngredientCategory.categories'
        db.delete_column(u'public_ingredientcategory', 'categories')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.IngredientCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.ingredientcategory': {
            'Meta': {'object_name': 'IngredientCategory'},
            'categories': ('django.db.models.fields.CharField', [], {'default': "'Meat'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_time': ('django.db.models.fields.CharField', [], {'default': "'in minutes'", 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Tell us about this Mancipe'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.TextField', [], {'default': "'How do we make this?'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prep_time': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']