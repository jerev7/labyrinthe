# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import Labyrinthe

class Carte:

	"""Objet de transition entre un fichier et un labyrinthe."""

	def __init__(self, nom, chaine):
		self.nom = nom
		self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine) #permet de lire la chaine pr former le labyrinthe

	
	def creer_labyrinthe_depuis_chaine(self, chaine): 
		"""
		creer un nouvel objet labyrinthe à partir de la chaine
		"""
		grille = chaine.split("\n")
		# on va créer le robot :
		
		nouveau_labyrinthe = Labyrinthe(grille) # à completer avec en attribut le robot
		return nouveau_labyrinthe # pour éviter que le nouveau labyrinthe ne se retrouve à la poubelle.
				


	def __repr__(self):
		return "<Carte {}>".format(self.nom)

