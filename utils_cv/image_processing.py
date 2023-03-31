import cv2
# Ce fichier contient la fonction resize_image, conv_gris, crop, crop_manual


def resize_image(img, dims, methode=cv2.INTER_CUBIC):
    '''
    Redimentionne l'image.

        Paramètres :
            img (image): Image deja chargée
            dims (couple d'entiers): Dimention voulue de l'image
    '''
    return cv2.resize(img, dims, interpolation=methode)


def conv_gris(img):
    '''
    Convertis l'image en niveaux de gris.

        Paramètres :
            img (image): Image deja chargée
    '''
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# La fonction crop prends en entrée un tuple, on peut remplacer celui-ci par 4 entiers en entrée si besoin


def crop(img, position):
    '''
    Découpe une sélection dans une image.

        Paramètres :
            img (image): Image deja chargée
            position (tuple=(x,y,w,h) avec x,y,w,h entiers): Position de la sélection, découpe de (x,y) à (x+w,y+h)
    '''
    x, y, w, h = position[0], position[1], position[2], position[3]
    crop = img[int(y):int(y + h), int(x):int(x+w)]
    return crop


def crop_manual(img):
    '''
    Découpe une sélection dans une image, la sélection est choisie avec la souris au moment de l'appel de la fonction.

        Paramètres :
            img (image): Image deja chargée
    '''

    (topleftX, topleftY, width, height) = cv2.selectROI("Window_name", img)
    crop = img[int(topleftY):int(topleftY + height),
               int(topleftX):int(topleftX+width)]
    return crop


def draw_rectangle(img, tlcorner, brcorner, color=(0, 0, 0), thickness=2, label="Fruit"):
    '''
    Dessine un rectangle sur l'image, l'emplacement du rectangle est saisi en entrée.

        Paramètres :
            img (image): Image deja chargée
            tlconer (tuple=(x,y)): Coordonnées du coint en haut a gauche
            brcorner(tuple=(x',y')): Coordonnées du coint en bas à droite
            color (tuple=(red,blue,green)): Couleur du rectangle, bleu par défaut
            thickness (entier): Epaisseur du rectangle, 3 par défaut
    '''
    image = cv2.rectangle(img, tlcorner, brcorner, color, thickness)
    label_coords = (tlcorner[0]+4, tlcorner[1]+24)
    cv2.putText(image, label, label_coords,
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, lineType=cv2.LINE_AA)
    return image


def select_box(img, color=(0, 255, 0), thickness=3):
    '''
    Dessine un rectangle sur l'image, l'emplacement du rectangle est choisi avec la souris au moment de l'appel de la fonction.

        Paramètres :
            img (image): Image deja chargée
            color (tuple=(red,blue,green)): Couleur du rectangle, bleu par défaut
            thickness (entier): Epaisseur du rectangle
    '''
    (topleftX, topleftY, width, height) = cv2.selectROI("Window_name", img)
    tl = (topleftX, topleftY)
    br = (topleftX + width, topleftY + height)
    rec = draw_rectangle(img, tl, br, color, thickness)
    return rec


FRUIT_TO_COST = {"apple_green": 0.2, "apple_red": 0.2, "apricot": 0.3, "avocado": 1.2, "banana": 0.2, "clementine": 0.15, "fig": 0.3,
                 "kiwi": 0.4, "onion_red": 0.15, "onion_white": 0.15, "pear": 0.25, "pepper_red": 0.3, "potato": 0.3, "strawberry": 0.1, "watermelon": 7.5}


def draw_multiple_rectangles(img, list_coord, list_label):
    for i in range(len(list_coord)):
        print(img.shape)
        tl = (list_coord[i][0], list_coord[i][1])
        br = (list_coord[i][0] + list_coord[i][2],
              list_coord[i][1] + list_coord[i][3])
        img = draw_rectangle(
            img, tl, br, label=list_label[i] + "Price: " + str(FRUIT_TO_COST[list_label[i]]) + " euros.")
    return img
