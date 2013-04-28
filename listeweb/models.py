# -*- coding: utf-8 -*-

from django.db import models

# Create your models here

class Boutique(models.Model):
    nom = models.CharField(max_length=255)
    rue = models.CharField(max_length=255, blank = True, null= True)
    code_postal = models.CharField(max_length=10,blank = True, null= True)
    ville = models.CharField(max_length=255,blank = True, null= True)
    telephone = models.CharField(max_length=15,blank = True, null= True)
    url = models.URLField(verbose_name="site web",blank = True, null= True)
    
    def __unicode__(self):
        return self.nom
    

class ArticleBase(models.Model):
    nom = models.CharField(max_length=255, verbose_name="nom du produit")
    photo = models.FileField(verbose_name="Photo",upload_to="img",blank = True, null= True)
    descriptif = models.TextField(verbose_name="Descriptif",blank = True, null= True)
    index = models.IntegerField(verbose_name="Index",blank = True, null= True)
    boutique =models.ManyToManyField(Boutique, verbose_name=u"Boutique",blank = True, null= True)
    publie = models.BooleanField(verbose_name="Publication")
    
    def __unicode__(self):
        return self.nom
    
    
class ArticleLien(models.Model):
    url = models.URLField(verbose_name="Lien vers article sur un site web")
    reference = models.ForeignKey(ArticleBase)

class ArticleGenerique(ArticleBase):
    quantite = models.IntegerField(verbose_name="Quantité")

class Article(ArticleBase):
    prix = models.FloatField(verbose_name="Prix")
    quantite = models.IntegerField(verbose_name="Quantité")
    
    def participations(self):
        return  ParticipationFinanciere.objects.filter(reference = self.id)
    
    def prix_total(self):
        return self.prix*self.quantite
    
    def montant_restant(self):
        montant_participation = 0
        for item in self.participations():
            montant_participation = montant_participation + item.montant
        
        return (self.prix*self.quantite) - montant_participation
    
    def nb_participations(self):
        return len(self.participations())
    
    
    
class ParticipationFinanciere(models.Model):
    montant = models.FloatField(verbose_name="Montant de la participation")
    nom_du_participant = models.CharField(max_length=255)
    reference = models.ForeignKey(Article)
    
class Participation(models.Model):
    quantite = models.IntegerField(verbose_name="Montant de la participation")
    nom_du_participant = models.CharField(max_length=255)
    reference = models.ForeignKey(ArticleGenerique)