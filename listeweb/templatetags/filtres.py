# -*- coding: utf-8 -*-

import os
from django import template
from django.conf import settings
from PIL import Image, ImageOps , ImageFilter ,ImageChops
from urlparse import urlparse

register = template.Library()

@register.filter(is_safe=True)
def hostname(url):
    return urlparse(url)[1]


@register.filter(is_safe=True)
def monnaie(nombre):
    if nombre == 0.0:
        return "Gratuit"
    else:
        nombre = "{0:10.2f}".format(nombre)
        nombre = str(nombre)+"€"
        nombre = nombre.replace(".", ",") 
        return nombre

@register.filter(is_safe=True)   
def resize(myfile, size='100x100x1'):
    try:
        
        path = myfile.path.replace(settings.MEDIA_ROOT,"") #TODO: trouver pkoi Image et Filebrowsefield renvoient des chemins différents
        path = settings.MEDIA_ROOT+path
        x, y, ratio = [int(x) for x in size.split('x')]
        filehead, filetail = os.path.split(path)
        basename, format = os.path.splitext(filetail)
        
        if format == ".png":
            format = ".jpg"
            
        miniature = basename + '_' + size + format
        filename = path
        filehead = os.path.join(filehead,'mini')
        if not os.path.exists(filehead):
            os.makedirs(filehead)
        miniature_filename = os.path.join(filehead, miniature)
        miniature_url = filehead + '/' + miniature
        
        if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
            os.unlink(miniature_filename)
    
        if not os.path.exists(miniature_filename):
           
            image = ImageOps.fit(Image.open(filename), (x,y), Image.ANTIALIAS)
              
            try:
                image.save(miniature_filename, "JPEG", quality=90, optimize=True, progressive=True)
            except:
                image.save(miniature_filename, "JPEG", quality=90)
            
        return miniature_url.replace(settings.MEDIA_ROOT,settings.MEDIA_URL)
    
    except:
        return "fileerror.jpg"