# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, grille):
		self.grille = grille
		for numero_ligne, ligne in enumerate(self.grille):
			if "X" in ligne:
				# On trouve la postion de X :
				self.robotY = numero_ligne
				ligne_liste = list(ligne)
				self.robotX = ligne_liste.index("X")
				# On efface le X initial :
				ligne_liste[self.robotX] = " "
				nouvelle_ligne = "".join(ligne_liste)
				self.grille[self.robotY] = nouvelle_ligne
		# on définit l'arrivée :		
		for numero_ligne, ligne in enumerate(self.grille):
			if "U" in ligne:
				self.arriveeY = numero_ligne
				ligne_liste = list(ligne)
				self.arriveeX = ligne_liste.index("U")

			
	def afficher_carte(self):
		
		for numero_ligne, ligne in enumerate(self.grille):
			if numero_ligne == self.robotY:
				ligne_liste = list(ligne)
				position_robot = self.robotX
				ligne_liste[position_robot] = "X"
				nouvelle_ligne = "".join(ligne_liste)
				print(nouvelle_ligne)
			else:
				print(ligne)	

		
	def deplacement(self):

		direction = input("choisissez votre direction puis appuyez sur 'Entrée' : \n")
		nbre_cases = input("choisissez le nombre de cases puis appuyez sur 'Entrée' : \n")
		direction = direction.lower()
		print(f"{direction}{nbre_cases}")
		
		if nbre_cases == "":
			nbre_cases = 1
		nbre_cases =int(nbre_cases)
		i = 0
		if direction == "n":
			while i < nbre_cases:
				self.robotY -= 1
				i += 1 
		elif direction == "s":
			while i < nbre_cases:
				self.robotY += 1
				i += 1
		elif direction == "e":
			while i < nbre_cases:
				self.robotX += 1
				i += 1
		elif direction == "o":
			while i < nbre_cases:
				self.robotX -= 1			
				i += 1
		self.afficher_carte()
