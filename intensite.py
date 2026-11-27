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
    liste_int = []
    liste_nm = [] 
    for i in range(len(longueurs_onde)) :
        if max_f > longueurs_onde[i] >= min_f :
            liste_int.append(intensites[i])
            liste_nm.append(longueurs_onde[i])
    dictionnaire[min_f] = {"intensité": liste_int, "nm": liste_nm} 
    
    min_f = max_f
    max_f = min_f + pas

#print(dictionnaire)
########################################### Affichage des données #########################################################

for min_f in dictionnaire :
    valeurs = dictionnaire[min_f]["intensité"]
    if len(valeurs) > 0 :
        v_num = len(valeurs)
        v_min = min(valeurs)
        v_max = max(valeurs)
        v_moy = sum(valeurs)/len(valeurs)

        print('la fenetre : ', min_f , "contient ", v_num, 'intensités' ,'la valeur minimum est', v_min , 'la valeur maximum est', v_max, "l'intensite moyenne est ", v_moy)

    else :
        print('Aucune intensité enregistré dans cette fenetre')