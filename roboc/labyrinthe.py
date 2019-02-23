# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, grille):
		self.robot = robot
		self.grille = grille
	
	def afficher_carte(self):
		print(self.grille) 
		
	def deplacement(self):

		direction = input("choisissez votre direction puis appuyez sur 'Entrée' : \n")
		nbre_cases = input("choisissez le nombre de cases puis appuyez sur 'Entrée' : \n")
		direction = direction.lower()
		for element in self.grille:
			print(element)
		print(f"{direction}{nbre_cases}")
		
		if nbre_cases == "":
			nbre_cases = 1
		nbre_cases =int(nbre_cases)
		i = 0
		if direction == "n":
			while i < nbre_cases:
				for numero_ligne, ligne in enumerate(self.grille):
					if "X" in ligne:
						ligne_liste = list(ligne)			
						position_robot = ligne_liste.index("X")
						ligne_robot = numero_ligne
						ligne_liste[position_robot] = " "
						self.grille[ligne_robot] = "".join(ligne_liste)
				
				destination = self.grille[ligne_robot - 1]
				destination_liste = list(destination)					
				destination_liste[position_robot] = "X"
				self.grille[ligne_robot - 1] = "".join(destination_liste)	
			

				#robot garde la même position dans la ligne mais va à la ligne du dessous 
				i += 1 
		elif direction == "s":
			while i < nbre_cases:
				for numero_ligne, ligne in enumerate(self.grille):
					if "X" in ligne:
						ligne_liste = list(ligne)			
						position_robot = ligne_liste.index("X")
						ligne_robot = numero_ligne
						ligne_liste[position_robot] = " "
						self.grille[ligne_robot] = "".join(ligne_liste)
				
				destination = self.grille[ligne_robot + 1]
				destination_liste = list(destination)					
				destination_liste[position_robot] = "X"
				self.grille[ligne_robot + 1] = "".join(destination_liste)

				#robot garde la même position dans la ligne mais va à la ligne du dessus 
				i += 1
		elif direction == "e":
			while i < nbre_cases:
				for numero_ligne, ligne in enumerate(self.grille):
					if "X" in ligne:
						ligne_liste = list(ligne)
						position_robot = ligne_liste.index("X")
						ligne_robot = numero_ligne
						ligne_liste[position_robot] = " "
						ligne_liste[position_robot + 1] = "X"
						self.grille[ligne_robot] = "".join(ligne_liste)
					

				#position robot dans la ligne += 1
				i += 1
		elif direction == "o":
			while i < nbre_cases:
				for numero_ligne, ligne in enumerate(self.grille):	
					if "X" in ligne:
							ligne_liste = list(ligne)
							position_robot = ligne_liste.index("X")
							ligne_robot = numero_ligne
							ligne_liste[position_robot] = " "
							ligne_liste[position_robot - 1] = "X"
							self.grille[ligne_robot] = "".join(ligne_liste)

			
				#postion_robot dans la ligne -= 1
				i += 1
		
		# On affiche les lignes modifié avec la nouvelle position de X		
		for element in self.grille:
			print(element)