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

        message = choice(hello_morning.objects.all()).text   + \
                  choice(what_morning.objects.all()).text    + \
                  choice(what_dejeuner.objects.all()).text   + \
                  choice(entree_str.objects.all()).text      + \
                  entree                                     + \
                  choice(plat_str.objects.all()).text        + \
                  choice(choice_str.objects.filter(nb_choice=len(plats))).text%tuple(plats) +\
                  choice(dessert_str.objects.all()).text     + \
                  dessert + "."

    else:
        plats = plates[day][typeOfMeal]

        message = choice(hello_dinner.objects.all()).text + \
                  choice(what_dinner.objects.all()).text + \
                  choice(choice_str.objects.filter(nb_choice=len(plats))).text%tuple(plats) + "."

    l.sayFood(message.encode('utf-8'), cfg.channels, cfg.token)
    print(message)
