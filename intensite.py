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

pas = int(sys.argv[2])
min_f = (min(longueurs_onde)//pas)*pas
max_f = min_f + pas

dictionnaire = {}

while min_f <= max(longueurs_onde) :
    fenetre = [] 
    for i in range(len(longueurs_onde)) :
        if max_f > longueurs_onde[i] >= min_f :
            fenetre.append(intensites[i])
    dictionnaire[min_f] = fenetre
    
    min_f = max_f
    max_f = min_f + pas


