import argparse
from utils_cv.load_data import *
from utils_cv.fruit_classification import *
from utils_cv.crop_objects import *
from utils_cv.fruit_cost import *


def main(image, process):
    '''
    Applique le processus choisi à l'image choisie

        Paramètres :
            image (image deja load): L'image à traiter
            process (string): Le procesus que l'on veut
    '''

    if process == "cost":
        cost = total_cost(image)

    elif process == "fruit_type_auto":
        for fruit_img in crop_objects(image):
            display_image(fruit_img)
            fruit = fruit_classify(fruit_img)
            print("Le fruit est: " + fruit)

    elif process == "fruit_type_manual":
        fruit = fruit_classify_manual(image)
        print("Le fruit est: " + fruit)

    elif process == "is_good":
        state_of_fruit = is_good(image)
        print("Le fruit est" + state_of_fruit)

    else:
        print(
            "Processus inconnu, processus possibles: [ cost | fruit_type | is_good ]")


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="Chemin vers l'image de fruit")
    ap.add_argument("-p", "--processing", required=True,
                    help="Processus possibles: [ cost | fruit_type_auto | fruit_type_manual | is_good ]")
    args = vars(ap.parse_args())

    fruit_filename = args["input"]
    fruit_image = load_image(fruit_filename)
    process = args["processing"]

    main(fruit_image, process)
