# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.cook_time'
        db.add_column(u'public_recipe', 'cook_time',
                      self.gf('django.db.models.fields.CharField')(default='in minutes', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.cook_time'
        db.delete_column(u'public_recipe', 'cook_time')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'calories': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '20'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.IngredientCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.CharField', [], {'default': "'How much?'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.ingredientcategory': {
            'Meta': {'object_name': 'IngredientCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_time': ('django.db.models.fields.CharField', [], {'default': "'in minutes'", 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description has been entered yet'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.TextField', [], {'default': "'How do we make this?'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prep_time': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']