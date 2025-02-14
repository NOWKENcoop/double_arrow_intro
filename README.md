# Double Arrows - Jeu en Python avec Pygame

## Description
Double Arrows est un jeu développé en Python en utilisant la bibliothèque Pygame. Il s'agit d'un jeu de tir en 1 contre 1 où deux joueurs s'affrontent en lançant des flèches tout en évitant les tirs adverses. Chaque joueur peut choisir un personnage et se battre jusqu'à ce que l'un d'eux perde toute sa barre de vie. Pour le moment je n'ai réalisé que la partie 1 contre 1 mais je ferai les autres fonctonalitées

## Fonctionnalités
- Sélection des personnages avant le combat.
- Deux joueurs peuvent s'affronter sur le même écran.
- Dégradé dynamique en arrière-plan.
- Affichage des barres de vie évolutives.
- Victoire déterminée lorsqu'un joueur perd toute sa vie.
- Interface graphique simple avec boutons interactifs.

## Technologies utilisées
- Python
- Pygame

## Installation
### Prérequis
- Python 3 installé
- Pygame installé (`pip install pygame`)

## Utilisation
# Double Arrows - Jeu Pygame

## Description
"Double Arrows" est un jeu de tir développé en Python utilisant la bibliothèque Pygame. Dans ce jeu, deux joueurs s'affrontent en contrôlant des personnages avec des flèches comme projectiles. Le but est de survivre et d'éliminer son adversaire tout en évitant les attaques ennemies.

## Installation
1. Clonez ce dépôt ou téléchargez les fichiers.
2. Assurez-vous d'avoir Python 3.x installé sur votre machine.
3. Installez les dépendances nécessaires avec la commande suivante :
   ```bash
   pip install pygame
   ```
4. Placez les images nécessaires dans le dossier approprié.
5. Exécutez le fichier principal (`main.py`) pour lancer le jeu.

## Fonctionnalités
- **Mode 1v1** : Affrontez un ami dans un combat de flèches.
- **Mode Entraînement** : Testez vos compétences contre un adversaire contrôlé par l'ordinateur.
- **Écran de chargement** : Attendez le démarrage du jeu avec une image de chargement.
- **Sélection des personnages** : Choisissez un personnage pour chaque joueur parmi une sélection d'images.
- **Système de barre de vie** : Suivez la santé des joueurs avec des barres de vie.
- **Dégradé dynamique** : Un joli dégradé de couleurs est dessiné en arrière-plan pour l'ambiance.

## Commandes
### Joueur 1
- **Déplacer** : `W` (haut), `S` (bas)
- **Tirer** : `O`

### Joueur 2
- **Déplacer** : Flèches directionnelles
- **Tirer** : `8`

## Modes
- **Entraînement** : Un joueur contrôle un personnage, l'autre est automatisé `J'ai initialisé au niveau professionel`.
- **1v1** : Affrontement direct entre deux joueurs humains.

## Images utilisées
Les images pour les personnages et l'interface sont chargées à partir des fichiers spécifiés dans le code.

## Aide
- Si vous avez besoin d'assistance pendant le jeu, consultez le menu d'aide pour des informations sur les commandes.
- Vous pouvez quitter le jeu en tout moment via le bouton "Quitter" dans le menu principal.

## Fonctionnement du code
Le code utilise Pygame pour gérer l'affichage, les événements du clavier et les interactions entre les éléments du jeu. Le gameplay repose sur une boucle principale qui gère les mouvements des joueurs, les tirs, les collisions, et l'affichage des informations à l'écran.

1. Exécutez le fichier principal du jeu :
   ```sh
   python double_arrow.py
   ```
2. Sélectionnez vos personnages.
3. Affrontez-vous en utilisant les touches de déplacement et de tir.
4. Le premier joueur à perdre toute sa barre de vie perd la partie.
5. Revenez au menu principal pour rejouer ou quitter.

## Contrôles
| Joueur | Monter | Descendre | Tirer |
|--------|--------|----------|-------|
| Joueur 1 | `W` | `S` | `O` |
| Joueur 2 | Flèche Haut | Flèche Bas | Pavé numérique `8` |

## Images et ressources
Les images du jeu sont placées dans un dossier `image/` situé dans le même répertoire que le script principal.

## Capture d'écran

> 
    principal 
![Capture d'écran de la simulation](https://github.com/NOWKENcoop/cartographie-lidar/blob/master/images.png)

> 
    play
![Capture d'écran de la simulation](https://github.com/NOWKENcoop/cartographie-lidar/blob/master/images.jpeg)


## Auteur
- **NDE WILLIAM**

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

