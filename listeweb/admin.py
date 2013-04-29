# -*- coding: utf-8 -*-

from django.contrib import admin
from django.template import defaultfilters
from listeweb.models import ArticleGenerique,Article,ArticleLien,Boutique,Participation,ParticipationFinanciere,\
    ArticleBase,TexteIntroduction
from tinymce.widgets import TinyMCE
from django.db import models


class TexteIntroductionAdmin(admin.ModelAdmin):

    formfield_overrides = {
          models.TextField : {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class ArticleLienInline(admin.TabularInline):
    model = ArticleLien

class ParticipationInline(admin.TabularInline):
    model = Participation

class ParticipationFinanciereInline(admin.TabularInline):
    model = ParticipationFinanciere
    
class ArticleGeneriqueAdmin(admin.ModelAdmin):
    list_display = [ 'nom', 'quantite', 'publie']
    search_fields = ['nom']
    fieldsets = [('Nom et infos', {'fields': ['nom', 'descriptif','quantite']}),
                 (None, {'fields': ['photo', 'boutique','index','publie']}),
                 ]

    filter_horizontal = ('boutique',)
    inlines = [
        ParticipationInline,ArticleLienInline,
    ]
    formfield_overrides = {
          models.TextField : {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class ArticleAdmin(admin.ModelAdmin):
    list_display = [ 'nom', 'prix', 'publie']
    search_fields = ['nom']
    fieldsets = [('Nom et infos', {'fields': ['nom', 'descriptif','quantite','prix']}),
                 (None, {'fields': ['photo', 'boutique','index','publie']}),
                 ]
    
    filter_horizontal = ('boutique',)
    inlines = [
        ParticipationFinanciereInline,ArticleLienInline,
    ]
    
    formfield_overrides = {
          models.TextField : {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

    
class BoutiqueAdmin(admin.ModelAdmin):
    list_display = [ 'nom', 'ville']



admin.site.register(ArticleGenerique, ArticleGeneriqueAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(TexteIntroduction, TexteIntroductionAdmin)