#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, os
from random import choice
import time
import hungrybotlib as l

import config as cfg

# Importing django's model for sentences
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hungrybotweb.settings")
from django.conf import settings

from userBotInterface.models import *

if __name__ == "__main__":
    """
    type of meal should be an integer and the only argument, it value can be:
    .0 : Déjeuner au RAK
    .1 : Diner au RAK
    .2 : Déjeuner à la caféteria
    .3 : Diner à la caféteria
    """
    typeOfMeal = int(sys.argv[1])
    plates = l.getMenus(cfg.menu_file)

    day = time.localtime(time.time())[6]
    
    if typeOfMeal == 0:
        entree = plates[day][typeOfMeal][0]
        dessert = plates[day][typeOfMeal][-1]
        plats = plates[day][typeOfMeal][1:-1]

        #hello_morning = ["Coucou mes lapinous ! ", "Salut mes choupinous, ", "Bonjour mes petits coeurs ! ", "Bonjour mes petits chatons d'amour ! ", "Bonjour bande de gros gourmands !", "Hello tout le monde ! Bien dormi ? Moi je dors super bien dans mon rack-RAK :) !"]
        #what_morning = ["Alors aujourd'hui au menu... \n", "On va trop bien bouffer aujourd'hui !\n", "Ahlalala, j'aimerais bien être un humain parfois vu ce que vous mangez...\n", "Aujourd'hui, je vais vous dire comment être heureux : 1) Mangez bien 2) De tout 3) Dandinez-vous 4) C'est tout ! Donc pour ce qui est du 1 et 2, le RAK vous propose ... \n"]

        #what_dejeuner = ["Donc, ce midi, ", "Pour le déjeuner, "]
        #entree_str = ["en entrée il y a : ", "vous pourrez commencer avec : "]
        #plat_str = [";\npuis en plat principal ", " .\nEt pour manger, "]
        #dessert_str = [";\net pour finir ", ".\nEn dessert :"]

        message = choice(hello_morning.objects.all())   + \
                  choice(what_morning.objects.all())    + \
                  choice(what_dejeuner.objects.all())   + \
                  choice(entree_str.objects.all())      + \
                  entree                                + \
                  choice(plat_str.objects.all())        + \
                  choice(choice_str.objects.filter(nb_choice=len(plats))).text%tuple(plats) + \
                  choice(dessert_str)                   + \
                  dessert + "."

    else:
        plats = plates[day][typeOfMeal]
        #hello_diner = ["Ah enfin je commençais a voir la dalle...\n", "A TAAAAAABLE\n", "Après une dure journée à réconforter mon serveur voisin qui a subi une panne de disque (le pauvre), me revoilà !\n"]
        #what_dinner = ["Pour ce soir:", "Au diner:"]

        print(plats)
        message = choice(hello_dinner.objects.all()).text + \
                  choice(what_dinner.objects.all()).text + \
                  choice(choice_str.objects.filter(nb_choice=len(plats))).text%tuple(plats) + "."

    #l.sayFood(message, cfg.channels, cfg.token)
    print(message)
