from Graphe import Graphe
import pygame

def selectionSommet(x, y ,g, joueur):
	"""
		entrée: la position cliquée à la souris, le graph, le joueur (sa couleur)
		sortie: renvoie le numéro du sommet, si on a bien cliqué et que le sommet est toujours blanc
			et -1 sinon
	"""
	for i in range(8):
		if g.circrect[i].collidepoint(x,y) == True and (g.color[i] == "white"):
			return i
	return -1

def testGagne(g, joueur):
	"""
		Entrée: le graph , le joueur (sa couleur)

		vérifie pour tous les sommets que
			si le sommet est blanc alors il n'y a pas de voisins de la couleur de joueur,
			sinon ce sommet n'est pas jouable
		renvoie True si il reste un sommet jouable pour joueur, et False sinon
	"""
	for i in range(8):
		if g.color[i] == "white":
			for j in g.adj[i]:
				if j == True:
					return True
	return False
