# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import Prestataire, Categorie



def index(request):
    try:
        prestataires = Prestataire.objects.all()
        cat_ascensoriste = Categorie.objects.get(slug=u"ascensoriste")
        cat_controleur = Categorie.objects.get(slug=u"bureau-de-controle")
        cat_bureau_etude = Categorie.objects.get(slug=u"bureau-detude")
        prest_audit=Prestataire.objects.filter(categorie__slug__contains=u'bureau-de-controle')
        prest_etude=Prestataire.objects.filter(categorie__slug__contains=u'bureau-detude')
        prest_asc=Prestataire.objects.filter(categorie__slug__contains=u'ascensoriste')

        context = {
            "prest_audit":prest_audit,
            "prest_asc":prest_asc,
            "prest_etude":prest_etude,
            "cat_ascensoriste":cat_ascensoriste,
            "cat_controleur":cat_controleur,
            "cat_bureau_etude":cat_bureau_etude,
        }

    except Prestataire.DoesNotExist,Categorie.DoesNotExist:
        context = {}

    return render(request,'prestataires/index.html',context)



def categorie(request, cat_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        categorie_prestataire = Categorie.objects.get(slug=cat_name_slug)
        context_dict['categorie'] = categorie_prestataire

        try:
            # essaie de prendre des prestataires dans cette catégorie
            prestataires=Prestataire.objects.filter(categorie=categorie_prestataire)
            context_dict['prestataires']=prestataires

        except Prestataire.DoesNotExist:
            pass

    except Categorie.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass


    # Go render the response and return it to the client.
    return render(request, 'prestataires/categorie.html', context_dict)

def prestataire(request, prest_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        prestataire = Prestataire.objects.get(slug=prest_name_slug)
        context_dict['prestataire'] = prestataire

    except Prestataire.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass


    # Go render the response and return it to the client.
    return render(request, 'prestataires/prestataire.html', context_dict)