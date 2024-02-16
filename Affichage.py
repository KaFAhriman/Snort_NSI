import pygame
from Graphe import Graphe

def creePlateau():
	g = Graphe(8)
	g.ajouterArc(0,1)
	g.ajouterArc(0,2)
	g.ajouterArc(0,6)
	g.ajouterArc(1,3)
	g.ajouterArc(1,7)
	g.ajouterArc(2,3)
	g.ajouterArc(2,4)
	g.ajouterArc(3,5)
	g.ajouterArc(4,5)
	g.ajouterArc(4,6)
	g.ajouterArc(5,7)
	g.ajouterArc(6,7)
	return g

def affichePlateau(fenetre, g, joueur, chaine):
	for i in range(len(g.adj)):
		for j in range(len(g.adj[0])):
			if g.getArc(i,j):
				pygame.draw.lines(fenetre, "white", True, [g.pos[i],g.pos[j]], 1)

	for i in range(len(g.color)):
		pygame.draw.circle(fenetre, g.color[i], g.pos[i], 20)


	font = pygame.font.SysFont("broadway",24,bold=False,italic=False)
	if joueur == "red":
		c = (255,255,0)
		text=font.render(chaine,1,c)
	else:
		c= (255, 0, 0)
		text=font.render(chaine,1,c)
	fenetre.blit(text,(30,30))

	pygame.display.flip()
