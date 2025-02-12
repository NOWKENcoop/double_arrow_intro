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
Les images du jeu doivent être placées dans un dossier `image/` situé dans le même répertoire que le script principal.


## Auteur
- **Votre Nom** - nowken

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

