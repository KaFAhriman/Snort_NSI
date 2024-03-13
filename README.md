# Rapport

## 1) Le problème:

Le projet se découpe en 4 fichiers: **Jeu-snort.py**, **Graphe.py**, **moteur.py** et **Affichage.py**

Chacun joue un rôle dans le bon fonctionnement du programme, **Jeu-snort** par exemple est le fichier principal, c'est le fichier qui lance le jeu et dans lequel tout les autres fichiers sont rassemblés.

Pourtant ce fichier n'est pas terminé, en effet comme écrit ci-dessus, il nécessite les fonctions contenues dans d'autre fichiers pour pouvoir faire plus qu'afficher le graphe.

Pour cela les fonctions dans le fichier **moteur.py** doivent être complétées.

## 2) La solution

### La fonction *selectionSommet*:

La fonction *selectionSommet* a comme but de vérifier si les coordonnées (x, y) de la souris entrent en collision avec un sommet, si c'est nous vérifions si le sommet est déjà sélectionné ou non. Dans ce cas là la fonction retournera le numéro du sommet, autrement elle devra renvoyer -1.

Pour détecter si la souris entre en collision avec le cercle représentant le sommet à l'écran, nous avons donc ajouter un nouvel attribut à la classe *Graphe*: la liste *circrect*. Cette liste contient un rectangle pour chaque sommet, ainsi nous pourrons détecter les collisions avec ces rectangles et

## 3) Améliorations possibles

### Nouveaux graphes
