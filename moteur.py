from Graphe import Graphe
import pygame

def selectionSommet(x, y ,g, joueur):
	"""
		entrée: la position cliquée à la souris, le graph, le joueur (sa couleur)
		sortie: renvoie le numéro du sommet, si on a bien cliqué et que le sommet est toujours blanc
			et -1 sinon
	"""
	for i in range(len(g.color)):
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
	for i in range(len(g.color)):
		if g.color[i] == 'white':
			v = []
			for j in range(len(g.color)):
				if g.adj[i][j] == True:
					if g.color[j] == joueur:
						v += [i]
			if v == []:
				return True
	return False
