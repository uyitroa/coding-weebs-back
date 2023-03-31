# Objectif de l'algorithme

Créer un algorithme qui :
+ Crop les objets
+ Détermine si l'objet est un fruit ou non
+ Si c'est un fruit, quel type de fruit c'est
+ Si c'est un fruit, est-ce qu'il est pourri ou non
+ Créer une interface graphique : un site par exemple

# Etape 1 : Base de données

Trouver une base de données de fruits, avec un fond.
Pistes : 
+ Fruits 360 : https://www.kaggle.com/datasets/moltean/fruits
Une dataset contenant 90380 images de fruits et légumes.
Problème : L'image est déjà crop.
Solution possible : Ajouter un fond soi-même artificiellement ?
+ Google image
Avantage : Beaucoup d'images, et assez représentatif d'images prises dans la vie réeele
Problème : Long à obtenir, et nécessite un tri manuel
+ ROCHA, Anderson; HAUAGGE, Daniel C.; WAINER, Jacques; GOLDENSTEIN, Siome. https://www.ic.unicamp.br/~rocha/pub/communications.html 
Une dataset avec 2,633 images de 15 fruits et légumes
+ GroceryStoreDataset : https://github.com/marcusklasson/GroceryStoreDataset
5125 images de 81 classes de fruits, légumes, et autres emballages (jus de fruit, lait, yaourt...). Il y a en fait 42 grandes classes (La grande classe pomme contient : pink lady, golden...)

...



### Qui s'en charge 
Erwin

# Etape 2 : Crop les objets

### Qui s'en charge
Hung

# Etape 3 : Déterminer si l'objet est un fruit ou non

### Qui s'en charge 
Xavier (aura peut etre de l'overlap avec étape 2, le programme pourra peut etre faire les deux en même temps)

# Etape 4 : Déterminer le type de fruit

### Qui s'en charge 
Yi


# Etape 5 : Déterminer si le fruit est pourri ou non

### Qui s'en charge 

# Etape 5.1 : Interface ligne de commande

### Qui s'en charge
Alexis

# Etape 6 : Créer une interface graphique

### Qui s'en charge
Hung


# Soutenance

### Présentation générale du projet et de ses fonctionnalités puis démo

### Présentation de l'organisation en sprint
1. Sprint 0: Motivation, Conception
1. Sprint 1: implémentation des modules de manipulation d'images
1. Sprint 2: Création de la base des données pour entraîner nos models
1. Sprint 3: Création des models et entraînement
1. Sprint 4: Finalisation du MVP avec une interface de ligne de commande (CLI) 
1. Sprint 5: Incrémentation: création d'un site web avec une interface graphique (GUI)

        Ce mini-projet est découpé en plusieurs objectifs, eux-même découpés en  sprints et fonctionnalités. La notion de sprint fait référence à la méthode agile. Un sprint correspond à un intervalle de temps pendant lequel l’équipe projet va compléter un certain nombre de tâches.

### Model 1: classification de fruits
1. Database fruit360
1. Model avec Resnet50 

### Model 2: crop auto des objets sur une image
1. Model Yolov4

### Model 3: fruit ou non et s'il est pourri
1. Model custom CNN

### Fonctionnalité coût

### Interface en ligne de commande

### Interface graphique et site web

### Feedback / Amélioration

