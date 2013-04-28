# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Boutique'
        db.create_table(u'listeweb_boutique', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rue', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'listeweb', ['Boutique'])

        # Adding model 'ArticleBase'
        db.create_table(u'listeweb_articlebase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('descriptif', self.gf('django.db.models.fields.TextField')()),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
            ('publie', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'listeweb', ['ArticleBase'])

        # Adding M2M table for field boutique on 'ArticleBase'
        db.create_table(u'listeweb_articlebase_boutique', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articlebase', models.ForeignKey(orm[u'listeweb.articlebase'], null=False)),
            ('boutique', models.ForeignKey(orm[u'listeweb.boutique'], null=False))
        ))
        db.create_unique(u'listeweb_articlebase_boutique', ['articlebase_id', 'boutique_id'])

        # Adding model 'ArticleLien'
        db.create_table(u'listeweb_articlelien', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listeweb.ArticleBase'])),
        ))
        db.send_create_signal(u'listeweb', ['ArticleLien'])

        # Adding model 'ArticleGenerique'
        db.create_table(u'listeweb_articlegenerique', (
            (u'articlebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['listeweb.ArticleBase'], unique=True, primary_key=True)),
            ('quantite', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'listeweb', ['ArticleGenerique'])

        # Adding model 'Article'
        db.create_table(u'listeweb_article', (
            (u'articlebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['listeweb.ArticleBase'], unique=True, primary_key=True)),
            ('prix', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'listeweb', ['Article'])

        # Adding model 'ParticipationFinanciere'
        db.create_table(u'listeweb_participationfinanciere', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('montant', self.gf('django.db.models.fields.FloatField')()),
            ('nom_du_participant', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listeweb.Article'])),
        ))
        db.send_create_signal(u'listeweb', ['ParticipationFinanciere'])

        # Adding model 'Participation'
        db.create_table(u'listeweb_participation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantite', self.gf('django.db.models.fields.IntegerField')()),
            ('nom_du_participant', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listeweb.ArticleGenerique'])),
        ))
        db.send_create_signal(u'listeweb', ['Participation'])


    def backwards(self, orm):
        # Deleting model 'Boutique'
        db.delete_table(u'listeweb_boutique')

        # Deleting model 'ArticleBase'
        db.delete_table(u'listeweb_articlebase')

        # Removing M2M table for field boutique on 'ArticleBase'
        db.delete_table('listeweb_articlebase_boutique')

        # Deleting model 'ArticleLien'
        db.delete_table(u'listeweb_articlelien')

        # Deleting model 'ArticleGenerique'
        db.delete_table(u'listeweb_articlegenerique')

        # Deleting model 'Article'
        db.delete_table(u'listeweb_article')

        # Deleting model 'ParticipationFinanciere'
        db.delete_table(u'listeweb_participationfinanciere')

        # Deleting model 'Participation'
        db.delete_table(u'listeweb_participation')


    models = {
        u'listeweb.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'listeweb.ArticleBase']},
            u'articlebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listeweb.ArticleBase']", 'unique': 'True', 'primary_key': 'True'}),
            'prix': ('django.db.models.fields.FloatField', [], {})
        },
        u'listeweb.articlebase': {
            'Meta': {'object_name': 'ArticleBase'},
            'boutique': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['listeweb.Boutique']", 'symmetrical': 'False'}),
            'descriptif': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'publie': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'listeweb.articlegenerique': {
            'Meta': {'object_name': 'ArticleGenerique', '_ormbases': [u'listeweb.ArticleBase']},
            u'articlebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listeweb.ArticleBase']", 'unique': 'True', 'primary_key': 'True'}),
            'quantite': ('django.db.models.fields.IntegerField', [], {})
        },
        u'listeweb.articlelien': {
            'Meta': {'object_name': 'ArticleLien'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listeweb.ArticleBase']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'listeweb.boutique': {
            'Meta': {'object_name': 'Boutique'},
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'listeweb.participation': {
            'Meta': {'object_name': 'Participation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_du_participant': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'quantite': ('django.db.models.fields.IntegerField', [], {}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listeweb.ArticleGenerique']"})
        },
        u'listeweb.participationfinanciere': {
            'Meta': {'object_name': 'ParticipationFinanciere'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant': ('django.db.models.fields.FloatField', [], {}),
            'nom_du_participant': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listeweb.Article']"})
        }
    }

    complete_apps = ['listeweb']