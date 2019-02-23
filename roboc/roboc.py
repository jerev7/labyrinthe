# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from labyrinthe import Labyrinthe


# On charge les cartes existantes
cartes = []

for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read() # un seul fichier dans contenu à chaque fois
			nouvelle_carte = Carte(nom_carte, contenu)
			cartes.append(nouvelle_carte) # le fichier est ajouté à la liste de cartes et on remonte au début du for


# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
	print("  {} - {}".format(i + 1, carte.nom))

numero_carte = input("entrez un numéro de labyrinthe pour commencer à jouer : ")
numero_carte = int(numero_carte)
choix_carte = cartes[numero_carte - 1]
choix_carte.labyrinthe.deplacement()


# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
