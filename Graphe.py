import pygame
"""
	Graphe représenté par une matrice d'adjacence
"""

class Graphe:
		"""
			Un graphe représenté par une matrice d'adjacence,
			où les sommets sont les entiers n= 0, 1, ... n-1
		 	dont les positions sont définies dans une liste,
		 	et les couleurs des sommets dans une liste.
		"""

		def __init__(self,n):
			self.n = n
			self.adj = [[False] * n for i in range(n)]
			self.pos = [(200,100),(600,100),(300,200),(500,200),(300,400),(500,400),(200,500),(600,500)]
			self.color = ["white" for i in range(n)]
			self.circrect = [pygame.Rect(self.pos[i][0] - 20, self.pos[i][1] - 20, 41, 41) for i in range(n)]

		def __str__(self):
			return str(self.adj)

		def ajouterArc(self, s1, s2):
			self.adj[s1][s2] = True
			self.adj[s2][s1] = True

		def position(self,n):
			if n == 8:
				return
			else:
				print("positions non définies dans graphs.py")
				return []

		def getPos(self,s):
			return self.pos[s]

		def getColor(self,s):
			return self.color[s]

		def setColor(self,s,couleur):
			self.color[s] = couleur

		def getArc(self, s1, s2):
			return self.adj[s1][s2]

		def getVoisins(self, s):
			v=[]
			for i in range(self.n):
				if self.adj[s][i]:
					v.append(i)
			return v

		def getDegre(self, s):
			return len(self.getVoisins(s))

		def nbArcs(self):
			n = 0
			for s in range(self.n):
				n += len(self.getVoisins(s))
			return n

		def supprimerArc(self, s1, s2):
			self.adj[s1][s2] = False
			self.adj[s2][s1] = False



if __name__ == "__main__":
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

	for i in range(8):
		print(g.getVoisins(i))


	print("degre: ", g.getDegre(0))
	print("nbArcs ", g.nbArcs())
	for ligne in g.adj:
		print(ligne)
	print(g.pos)

	g.setColor(2,"blue")
	print(g.color)
