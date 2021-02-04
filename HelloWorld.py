 fichier = open("data.txt","r")
    #w pour écrire (nouveau, écrase si existant), #a pour écrire en ajout , #r pour lire

lignes = fichier.readlines()
for lignes in lignes:
    print(ligne)
fichier.close