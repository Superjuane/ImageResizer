# To install:
# pyinstaller --noconfirm --onedir --windowed --icon "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/sol.ico" --name "PreparadorDeImagenes" --upx-dir "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src" --add-data "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src/ImageResizer.py;." --paths "C:/Python39/lib/site-packages" --paths "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/ImagePreparatorPython/Lib/site-packages"  "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src/main.py"


import PySimpleGUI as sg
import os.path
from PIL import Image, ImageTk
import ImageResizer as ir


def Warning(msg):
    sg.Popup(msg, keep_on_top=True)


if __name__ == '__main__':

    listUploads = []

    layout0 = [
        [
            sg.Text("Elija que función utilizar", pad=(75, 4)),
        ],
        [
            sg.Button("PREPARAR IMAGENES", pad=(75, 0)),
        ],
        [
            sg.Button("SUBIR IMAGEN DIRECTAMENTE", pad=(55, 0)),
        ]
    ]

    imageResizerColumn = [
        [
            sg.Button("Atrás"),
        ],
        [
            sg.Text("Carpeta:"),
            sg.In(size=(60, 1), enable_events=True, key="-FOLDER1-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(70, 20), key="-FILE LIST-"
            )
        ],
        [sg.Button('Convierte la carpeta completa'), ],
        [sg.Button('Convierte la imagen'), ],
    ]

    image_viewer_column = [

        [sg.Text(size=(20, 1), key="-TEXT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    layout1 = [[sg.Column(imageResizerColumn),
                sg.VSeperator(),
                sg.Column(image_viewer_column),
                ]]

    headerPreparerColumn = [
        [
            sg.Button("Atras"),
        ],
        [
            sg.Text("Carpeta:"),
            sg.In(size=(60, 1), enable_events=True, key="-FOLDER2-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(70, 20), key="-FILE LIST2-"
            )
        ],

    ]

    layout2 = [[sg.Column(headerPreparerColumn)]]

    layout = [
        [
            sg.Column(layout0, key='-LAYOUT0-'),
            sg.Column(layout1, visible=False, key='-LAYOUT1-'),
            sg.Column(layout2, visible=False, key='-LAYOUT2-'),
        ]
    ]

    window = sg.Window("Eugenia Pintura - Subir Imagenes", layout,
                       icon=r'C:\Users\Juane Olivan\Documents\Eugenialazaro.com\repositorioImagenes\sol.ico',
                       size=(350, 200), location=(550, 75))

    layoutActual = "LAYOUT0"
    selected = False
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == 'PREPARAR IMAGENES':
            window[f'-LAYOUT0-'].update(visible=False)
            layoutActual = "LAYOUT1"
            window.move(75, 75)
            window.size = (1200, 500)
            window[f'-LAYOUT1-'].update(visible=True)

        if event == "SUBIR IMAGEN DIRECTAMENTE":
            window[f'-LAYOUT0-'].update(visible=False)
            layoutActual = "LAYOUT2"
            window.move(350, 75)
            window.size = (800, 500)
            window[f'-LAYOUT2-'].update(visible=True)

        elif event == "Atrás":
            window[f'-' + layoutActual + '-'].update(visible=False)
            layoutActual = "LAYOUT0"
            window.move(550, 75)
            window.size = (350, 200)
            window[f'-LAYOUT0-'].update(visible=True)

        elif event == "Atras":
            window[f'-' + layoutActual + '-'].update(visible=False)
            layoutActual = "LAYOUT0"
            window.move(550, 75)
            window.size = (350, 200)
            window[f'-LAYOUT0-'].update(visible=True)

        if event == "-FOLDER1-":
            folder = values["-FOLDER1-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".jpeg", ".gif", ".jpg", ".png", ".PNG"))
            ]
            window["-FILE LIST-"].update(fnames)

        if event == "-FOLDER2-":
            folder = values["-FOLDER2-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".jpeg", ".gif", ".jpg", ".png", ".PNG"))
            ]
            i = 0
            fnames2 = fnames
            for f in fnames:
                if i % 2 != 0: fnames2.remove(f)
                i += 1

            window["-FILE LIST2-"].update(fnames2)

        if event == 'Convierte la carpeta completa':
            try:
                ir.imageResizerFolder(values["-FOLDER1-"], "")
            except NameError:
                Warning("Error: No se ha seleccionado ninguna carpeta a procesar")

        if event == 'Convierte la imagen':
            if not selected:
                Warning("Nada seleccionado")
            else:
                clicked = sg.PopupOKCancel("Quieres procesar la imagen " + values["-FILE LIST-"][0])
                if clicked == 'OK':
                    try:
                        ir.imageResizerFile(values["-FILE LIST-"][0], values["-FOLDER1-"])
                    except NameError:
                        Warning("Error: No se ha seleccionado ninguna foto a convertir")
                elif clicked == 'Cancel':
                    pass
                elif clicked == None:
                    pass

        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            selected = True
            try:
                folder = values["-FOLDER1-"]
                filename = os.path.join(values["-FOLDER1-"], values["-FILE LIST-"][0])
                image = Image.open(filename)  # I prefer /
                image.thumbnail((500, 500))
                window["-IMAGE-"].update(
                    data=ImageTk.PhotoImage(image)
                )

            except:
                pass

    window.close()
