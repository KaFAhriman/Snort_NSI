# Rapport

## 1) Le problème:

Le projet se découpe en 4 fichiers: **Jeu-snort.py**, **Graphe.py**, **moteur.py** et **Affichage.py**

Chacun joue un rôle dans le bon fonctionnement du programme, **Jeu-snort.py** par exemple est le fichier principal, c'est le fichier qui lance le jeu et dans lequel tout les autres fichiers sont rassemblés.

Pourtant ce fichier n'est pas terminé, en effet comme écrit ci-dessus, il nécessite les fonctions contenues dans d'autre fichiers pour pouvoir faire plus qu'afficher le graphe.

Pour cela les fonctions dans le fichier **moteur.py** doivent être complétées.

## 2) La solution

### La fonction *selectionSommet()*:

La fonction *selectionSommet()* a comme but de vérifier si les coordonnées (x, y) de la souris entrent en collision avec un sommet, si c'est nous vérifions si le sommet est déjà sélectionné ou non. Dans ce cas là la fonction retournera le numéro du sommet, autrement elle devra renvoyer -1.

Pour détecter si la souris entre en collision avec le cercle représentant le sommet à l'écran, nous avons donc ajouter un nouvel attribut à la classe *Graphe*: la liste *circrect*. Cette liste contient un rectangle pour chaque sommet, ainsi nous pourrons détecter les collisions avec ces rectangles et

### La fonction *testGagne()*:

La fonction *testGagne()* vérifie si il reste un sommet jouable pour le joueur dont la couleur a été passée en argument.

Pour cela nous parcourons l'ensemble des sommets à l'aide d'une boucle *for*, ainsi si le sommet de rang *i* est blanc, nous créons une liste *v* enregistrant chacun des voisins de la couleur du joueur. Pour enregistrer ces voisins nous parcourons à nouveau l'ensemble des sommets, nous vérifions ensuite si il existe un arc entre le sommet *i* et le sommet *j* à l'aide de la matrice d'adjacence. Si cet arc existe et que le sommet *j* est de la couleur de joueur alors nous l'ajoutons à notre liste *v*. Après avoir parcouru la liste des sommets, si la liste v est vide, c'est que le sommet de rang *i* ne possède aucun voisin de la même couleur nous retournons donc *True*. Sinon la fonction renverra *False* dans tout les cas.

### La fonction sommetValide():

Cette fonction fut jugée superflue et embarrassante par l'ensemble du groupe, son contenu fut donc passée dans le fichier *Jeu-snort.py*. Elle servait originellement à déterminer si un joueur pouvait colorier un sommet.

Ainsi nous regardons parmi tout les sommets voisins du sommet sélectionné si il en existe un de la même couleur. Si oui alors le sommet n'est pas jouable et nous laissons le joueur en choisir un nouveau, sinon nous affectons au sommet la couleur du joueur et passons au joueur suivant. 

## 3) Améliorations possibles

### Nouveaux graphes

Il aurait été possible d'ajouter d'autre graphes afin de rendre le jeu plus intéressant pour les joueurs, celui-ci est en effet relativement simple.

### Collisions

Notre manière de détecter des collisions entre la souris et le sommet est fonctionnelle en l'état mais pas optimale : il est possible (bien que peu probable) que le joueur clique dans le rectangle sans cliquer sur le cercle, le rectangle étant plus grand que ce cercle.
