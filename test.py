fichier = open("data.txt", "r")


lignes = fichier.readlines()
for ligne in lignes:
    print(ligne)
fichier.close()


print("ceci est un test")