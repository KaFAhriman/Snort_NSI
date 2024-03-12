from Graphe import Graphe
import pygame

def selectionSommet(x, y ,g, joueur):
	"""
		entrée: la position cliquée à la souris, le graph, le joueur (sa couleur)
		sortie: renvoie le numéro du sommet, si on a bien cliqué et que le sommet est toujours blanc
			et -1 sinon
	"""
	for i in range(g.n):
		if (g.circrect[i].collidepoint(x,y) == True) and (g.color[i] == "white"): #vérifie si la position de la souris se trouve dans
			#print(i)
			return i
	return -1

#Fonction sommetValide jugée superflue et dont le contenu se trouve donc dans Jeu-snort.py

def testGagne(g, joueur):
	"""
		Entrée: le graph , le joueur (sa couleur)

		vérifie pour tous les sommets que
			si le sommet est blanc alors il n'y a pas de voisins de la couleur de joueur,
			sinon ce sommet n'est pas jouable
		renvoie True si il reste un sommet jouable pour joueur, et False sinon
	"""
	for i in range(g.n):
		if g.color[i] == 'white':
			v = [] #voisins de la couleur de joueur
			for j in range(g.n):
				if g.adj[i][j] == True:
					if g.color[j] == joueur:
						v += [i]
						#print(v)
			if v == []: #si il n'y a pas de voisins de la couleur de joueur
				return True #alors il reste un sommet jouable

	return False #sinon il n'en reste pas
