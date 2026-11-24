import os, re, sys

########################### Extraction des données ##############################################

longueurs_onde = [] #colonne 1
intensites = [] #colonne 2
donnees = False #initialisation pour rentrer dans la boucle

fichier = open(sys.argv[1])

for ligne in fichier :
    if ">>>>>Begin Spectral Data<<<<<" in ligne :
        donnees = True
    elif ">>>>>End Spectral Data<<<<<" in ligne :
        donnees = False
    elif donnees :
        colonnes = ligne.split()
        longueurs_onde.append(float(colonnes[0]))
        intensites.append(float(colonnes[1]))



########################### Création du dictionnaire ###########################################

min = 330
max = min + 10

fenetre_10 = []

