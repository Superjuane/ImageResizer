import glob
from PIL import Image


def prepare(name):
    end = 0
    if name.endswith(".png"):
        name = name.rstrip(".png")
        end = 1
    elif name.endswith(".jpeg"):
        name = name.rstrip(".jpeg")
        end = 2
    elif name.endswith(".jpg"):
        name = name.rstrip(".jpg")
        end = 3
    elif name.endswith(".gif"):
        name = name.rstrip(".gif")
        end = 4

    return name, end;

def formatoEnd(end):
    name = ""
    if end == 1: name += ".png"
    elif end == 2: name += ".jpeg"
    elif end == 3: name += ".jpg"
    elif end == 4: name += ".gif"
    return name


def imageResizerFile(image1, path1):
    if image1 == "":
        raise NameError("No hay una imagen seleccionada")
    path2 = "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES(proc)/"
    x, n = prepare(image1)
    image = Image.open(path1 + "/" + x + formatoEnd(n))
    imageBig = image.resize((1000, 800))
    imageSmall = image.resize((521, 371))
    imageBig.save(path2 + x + "-big"+formatoEnd(n))
    imageSmall.save(path2 + x + "-small"+formatoEnd(n))

def imageResizerFolder(path1, path2):
    if path1 == "":
        raise NameError("No hay un path seleccionado")
    # path1 = "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES (sin proc.)/"
    # print(path1)
    # print(path1 + "/" + "*.jpg")
    images = glob.glob(path1 + "/" + "*.jpg")
    images += glob.glob(path1 + "/" + "*.png")
    images += glob.glob(path1 + "/" + "*.gif")
    images += glob.glob(path1 + "/" + "*.jpeg")

    # for x in images:
    #     print(x)

    path2 = "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/IMAGENES(proc)/"
    for x in images:
        x = x.lstrip(path1)
        x = x.lstrip("\\")
        x, n = prepare(x)
        image = Image.open(path1 + "/" + x + formatoEnd(n))
        imageBig = image.resize((1000, 800))
        imageSmall = image.resize((521, 371))
        imageBig.save(path2 + x + "-big" + formatoEnd(n))
        imageSmall.save(path2 + x + "-small" + formatoEnd(n))
        print(path2 + x + "-big"+formatoEnd(n))
