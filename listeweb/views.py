# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response , redirect , get_object_or_404,\
    get_list_or_404# Create your views here.

from listeweb.models import Article,ArticleGenerique

def Home(request):
    articles = Article.objects.all().select_related().prefetch_related().filter(publie=True).order_by('index')
    articlesgeneriques = ArticleGenerique.objects.all().select_related().prefetch_related().filter(publie=True).order_by('index')
    
    return render_to_response('listeweb/listearticle.html', {'articles' : articles, 'articlesgeneriques':articlesgeneriques})
    
    