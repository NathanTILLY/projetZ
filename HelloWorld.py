fichier = open("HelloWorld.txt","r")

lignes = fichier.readlines()
for ligne in lignes:
    print(ligne , end = "")
fichier.close