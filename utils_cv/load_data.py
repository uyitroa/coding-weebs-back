import cv2


def load_and_display_image(filename):
    '''
    Charge et affiche l'image. (Prends en entrée le nom du fichier)
    L'image se ferme après que l'on appuie sur une touche

        Paramètres :
            filename (string): Le chemin vers le fichier
    '''
    img = cv2.imread(filename)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def load_image(filename):
    '''
    Charge l'image et la renvoie. (Prends en entrée le nom du fichier)

        Paramètres :
            filename (string): Le chemin vers le fichier
    '''
    return cv2.imread(filename)



def display_image(img):
    '''
    Affiche une image. (Prends en entrée une image deja chargée)

        Paramètres :
            img : l'image
    '''
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
