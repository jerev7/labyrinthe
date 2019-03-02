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
		# On définit les limites de la carte :
		
		for numero_ligne, ligne in enumerate(self.grille):
			self.ligne_liste = list(ligne)
			self.limite_est = len(ligne_liste) - 1
			self.limite_ouest = 1
			self.limite_nord = 1
		self.limite_sud = numero_ligne	 


			
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
			if self.robotY >= self.limite_nord:
				while i < nbre_cases:
					self.robotY -= 1
					i += 1
			else:
				print("limites de la carte atteintes...") 
		elif direction == "s":
			if self.robotY < self.limite_sud:
				while i < nbre_cases:
					self.robotY += 1
					i += 1
			else:
				print("limites de la carte atteintes...")		
		elif direction == "e":
			if self.robotX <= self.limite_est:
				while i < nbre_cases:
					self.robotX += 1
					i += 1
			else:
				print("limites de la carte atteintes...")
		elif direction == "o":
			if self.robotX >= self.limite_ouest:
				while i < nbre_cases:
					self.robotX -= 1			
					i += 1
			else:
				print("limites de la carte atteintes...")
		self.afficher_carte()