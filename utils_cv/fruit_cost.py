from utils_cv.crop_objects import *
from utils_cv.load_data import *
from utils_cv.fruit_classification import *

'''
Cout des fruits:

- Pomme_rouge 0.2 euros
- Pomme_verte 0.2 euros
- Abricot 0.3 euros
- Banane 0.2 euros
- Clementine 0.15 euros
- Figue 0.3 euros
- Oignon_rouge 0.15 euros
- Oignon_blanc 0.15 euros
- Poire 0.25 euros
- Kiwi 0.4 euros
- Avocat 1.2 euros
- Poivron_rouge 0.3 euros
- Pomme_de_terre 0.3 euros
- Fraise 0.1 euros
- Pasteque 7.5 euros

'''

FRUIT_TO_COST = {"apple_green": 0.2, "apple_red": 0.2, "apricot": 0.3, "avocado": 1.2, "banana": 0.2, "clementine": 0.15, "fig": 0.3,
                 "kiwi": 0.4, "onion_red": 0.15, "onion_white": 0.15, "pear": 0.25, "pepper_red": 0.3, "potato": 0.3, "strawberry": 0.1, "watermelon": 7.5}


def panier_compact(panier):
    compact = {}
    for fruit in panier:
        compact[fruit] = 0
    for fruit in panier:
        compact[fruit] = compact[fruit] + 1
    return compact


def total_cost(img):
    total_cost = 0
    panier = []
    for fruit_img in crop_objects(img):
        display_image(fruit_img)
        fruit = fruit_classify(fruit_img)
        total_cost = total_cost + FRUIT_TO_COST[fruit]
        print("Le fruit est: " + fruit)
        panier.append(fruit)
    compact = panier_compact(panier)
    cost_round = round(total_cost, 2)
    print("Total cost: " + str(cost_round) +
          " euros. Your fruits: " + str(compact))
