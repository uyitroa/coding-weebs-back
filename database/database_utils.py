import glob
import os
from pathlib import Path
import requests
import mimetypes
import shutil
from concurrent.futures import ThreadPoolExecutor


def addPrefix(folderPath, prefix):
    '''
    Itère récursivement sur tous les fichiers du dossier en paramètre, et ajoute le préfixe s'il n'est pas présent.
    '''
    for filePath in glob.iglob(folderPath + '**/**', recursive=True):
        
        if not os.path.isfile(filePath):
            continue

        fileName = os.path.basename(filePath)

        if fileName == "infos.md" or fileName == "database_utils.py":
            continue

        fileParentPath = os.path.dirname(filePath)
        fileParentName = os.path.basename(fileParentPath)
        fileParentPrefix = str.replace(fileParentName, " ", "_")
        if not fileName.startswith(prefix):
            nouvPath = os.path.join(fileParentPath, prefix+fileParentPrefix+fileName)
            print(filePath, nouvPath)
            os.rename(filePath, nouvPath)

def downloadImgFromUrl(url, folderPath, fileName):
    '''
    Télécharge l'image depuis une url

    Paramètres :
        url (string): l'url
        folderPath (string): Le chemin du dossier où l'on va télécharger l'image
        fileName (string): Le nom du fichier, sans l'extension
    '''
    try:
        # try to download the image
        r = requests.get(url, timeout=60)

        # save the image to disk

        content_type = r.headers['content-type']
        extension = mimetypes.guess_extension(content_type)

        if(extension == ".html" or extension == ".gif"):
            print("Wrong extension, skip")
            return

        with open(folderPath+"/raw/"+fileName+extension, "wb") as f:
            f.write(r.content)
        # update the counter
        print("[INFO] downloaded:", fileName, url)
    # handle if any exceptions are thrown during the download process
    except Exception as e:
        print("[WARNING] error downloading ", fileName, url,", skipping")
        # print("[WARNING]", e)


def downloadUrls(urlPath):
    '''
    Télécharge toutes les images d'un fichier contenant une url par ligne, dans le dossier où est situé le fichier

    Paramètres :
        filename (string): le chemin du fichier
    '''
    folderPath = os.path.dirname(urlPath)
    Path(folderPath + "/raw").mkdir(parents=True, exist_ok=True)        

    with open(urlPath, 'r', encoding='utf-8') as file:
        urls = file.read().splitlines()

        NB_PHOTOS = 3000000
        INDEX_DEBUT = 0
        
        iPos = 0
        with ThreadPoolExecutor(max_workers=20) as exe:
            for url in urls:
                if(iPos < INDEX_DEBUT):
                    iPos += 1
                    continue
                iPos += 1
                if(iPos-INDEX_DEBUT >= NB_PHOTOS):
                    break
                exe.submit(downloadImgFromUrl, url, folderPath, str(iPos))

addPrefix("/home/erwin/Documents/PERSO/Cours/CS 2022-23/Cours/Coding weeks/Semaine 2/database_renamed/fruits360/", "fruits360_")