import glob
from PIL import Image



def imageResizer(path1, path2):
    path1 = "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES (sin proc.)/"
    images = glob.glob(path1+"*.jpeg")
    path2 = "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES(proc)/"
    for x in images:
        x = x.lstrip("C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES (sin proc.)")
        x = x.lstrip("\\")
        x = x.rstrip(".jpeg")
        image = Image.open(path1 + x + ".jpeg")
        imageBig = image.resize((1000, 800))
        imageSmall = image.resize((521, 371))
        print(path2 + x + "-big.jpeg")
        imageBig.save(path2 + x + "-big.jpeg")
        imageSmall.save(path2 + x + "-small.jpeg")
