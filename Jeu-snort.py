import pygame
from pygame import *
from Affichage import *
from moteur import *
import traceback
"""
	Ouvre la fenêtre pygame,
	génère le graphe,
	affiche le graphe dans la fenetre pygame
	lance l'écouteur d'événement.
"""



pygame.init()
#
# Le rectangle est repéré en haut à gauche
fenetre= pygame.display.set_mode((800,600))
fenetre.fill((0,0,0))
chaine = "Au suivant"
joueur = "red"
g = creePlateau()
affichePlateau(fenetre, g, "yellow", chaine)
continuer =1

while continuer:
	for event in pygame.event.get():       #pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type == MOUSEBUTTONUP:
			(x,y) = event.pos
			#print(x,y)
			pygame.event.wait()
		elif event.type == MOUSEBUTTONDOWN:
			(x,y) = event.pos
			#print(x,y)
			sommet = selectionSommet(x, y , g, joueur)

			if(sommetValide(sommet, g, joueur)):
				print("Sommet valide ok")
			else:
				print("Sommet pas ok")
				print(joueur, "ne peux pas jouer là")
				break
			affichePlateau(fenetre, g, joueur, chaine)
			if testGagne(g, joueur):
				continuer = 1
			else:
				chaine = joueur + "    a perdu!!!!!"
				if joueur == "red":
					joueur = "yellow"
				else:
					joueur = "red"
				if testGagne(g, joueur):
					chaine = " MATCH NUL!!"

				#print("perdu")
				continuer = 0

			if joueur == "red":
				joueur = "yellow"
			else:
				joueur = "red"


continuer = 1
while continuer:

	fenetre.fill((0,0,0))
	affichePlateau(fenetre, g, joueur, chaine)
	for event in pygame.event.get():       #pygame.event.get():
		if event.type == QUIT:
			continuer = 0
	#else:



pygame.quit()
exit()
