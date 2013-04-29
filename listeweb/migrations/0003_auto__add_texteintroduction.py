# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TexteIntroduction'
        db.create_table(u'listeweb_texteintroduction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('participation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'listeweb', ['TexteIntroduction'])


    def backwards(self, orm):
        # Deleting model 'TexteIntroduction'
        db.delete_table(u'listeweb_texteintroduction')


    models = {
        u'listeweb.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'listeweb.ArticleBase']},
            u'articlebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listeweb.ArticleBase']", 'unique': 'True', 'primary_key': 'True'}),
            'prix': ('django.db.models.fields.FloatField', [], {}),
            'quantite': ('django.db.models.fields.IntegerField', [], {})
        },
        u'listeweb.articlebase': {
            'Meta': {'object_name': 'ArticleBase'},
            'boutique': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['listeweb.Boutique']", 'null': 'True', 'blank': 'True'}),
            'descriptif': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
        },
        u'listeweb.texteintroduction': {
            'Meta': {'object_name': 'TexteIntroduction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation': ('django.db.models.fields.TextField', [], {}),
            'texte': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['listeweb']