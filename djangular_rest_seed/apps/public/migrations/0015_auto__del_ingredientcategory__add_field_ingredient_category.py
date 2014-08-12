# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'IngredientCategory'
        db.delete_table(u'public_ingredientcategory')

        # Adding field 'Ingredient.category'
        db.add_column(u'public_ingredient', 'category',
                      self.gf('django.db.models.fields.CharField')(default='Meat', max_length=50),
                      keep_default=False)

        # Removing M2M table for field category on 'Ingredient'
        db.delete_table(db.shorten_name(u'public_ingredient_category'))


    def backwards(self, orm):
        # Adding model 'IngredientCategory'
        db.create_table(u'public_ingredientcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categories', self.gf('django.db.models.fields.CharField')(default='Meat', max_length=50)),
        ))
        db.send_create_signal(u'public', ['IngredientCategory'])

        # Deleting field 'Ingredient.category'
        db.delete_column(u'public_ingredient', 'category')

        # Adding M2M table for field category on 'Ingredient'
        m2m_table_name = db.shorten_name(u'public_ingredient_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredient', models.ForeignKey(orm[u'public.ingredient'], null=False)),
            ('ingredientcategory', models.ForeignKey(orm[u'public.ingredientcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ingredient_id', 'ingredientcategory_id'])


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'Meat'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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