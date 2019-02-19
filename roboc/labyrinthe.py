# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, grille):
		self.robot = robot
		self.grille = grille
		
		print("un labyrinthe a été créé\n")
		print(grille)

		


# déplacement du robot :

# N : aller au nord
# E : aller à l'est
# S : aller au sud
# O : aller vers l'ouest
# On peut rajouter un chiffre pr avancer de plusieurs cases ( ex : N3 aller de 3 cases vers le nord)

def deplacement():
	"""
	fonction pour déplacer le robot
	"""
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
			print("robot va vers le nord")
			i += 1 
	elif direction == "s":
		while i < nbre_cases:
			print("robot va vers le sud")
			i += 1
	elif direction == "e":
		while i < nbre_cases:
			print("robot va vers l'est")
			i += 1
	elif direction == "o":
		while i < nbre_cases:
			print("robot va vers l'ouest")
			i += 1


"""
