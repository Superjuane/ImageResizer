# \t                    Tab
# \\                    Inserts a back slash (\)
# \'                    Inserts a single quote (')
# \"                    Inserts a double quote (")
# \n                    New line

def getTipus(name):
    result = "Otro"
    if "Cartel" in name: result = "Cartel"
    elif "mesaSilla" in name: result = "mesaSilla"
    elif "bandeja" in name: result = "Bandejas"
    elif "silla" in name: result = "Sillas"
    elif "caja" in name: result = "Cajas"
    return result

def getTipusName(name):
    result = "Otro"
    if "Cartel" in name: result = "Cartel"
    elif "mesaSilla" in name: result = "Mesa y sillas"
    elif "bandeja" in name: result = "Bandejas"
    elif "silla" in name: result = "Sillas"
    elif "caja" in name: result = "Cajas"
    return result

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

    name += "-small"

    if(end == 1): name += ".png"
    elif (end == 2): name += ".jpeg"
    elif (end == 3): name += ".jpg"
    elif (end == 4): name += ".gif"

    return name

def headerBuilder(name, titulo):
    print(name)
    name = prepare(name)
    print(name)
    name2 = name.replace("small", "big")
    tipo = getTipus(name)
    nombreTipo = getTipusName(name)
    result = "< div class =\"col-1-3 mix " + tipo + "\" >"
    result += "\n\t< div class =\"content\" >"
    result += "\n\t\t< div class =\"recent-work\" >"
    result += "\n\t\t\t< img src = \"images/workE/" + name + "\" alt = \"\" >"
    result += "\n\t\t\t< div class =\"overlay\" >"
    result += "\n\t\t\t\t< span > " + nombreTipo + " < / span >"
    result += "\n\t\t\t\t< h2 > < a class =\"img-wrap\" data-rel=\"lightcase:"+ tipo +"\" title=\""+titulo+" - "+nombreTipo+"\" href=\"images/workE/"+name2+"\" > "+titulo+" < / a > < / h2 >"
    result += "\n\t\t\t< / div >"
    result += "\n\t\t< / div >"
    result += "\n\t< / div >"
    result += "\n< / div >"
    print(result)

if __name__ == '__main__':
    headerBuilder("Cartel-1.png", "Bones Festes")
    headerBuilder("mesaSilla-2.png", "Mesa-Pizarra")
