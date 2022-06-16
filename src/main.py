# To install:
# pyinstaller --noconfirm --onedir --windowed --icon "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/repositorioImagenes/sol.ico" --name "PreparadorDeImagenes" --upx-dir "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src" --add-data "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src/ImageResizer.py;." --paths "C:/Python39/lib/site-packages" --paths "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/ImagePreparatorPython/Lib/site-packages"  "C:/Users/Juane Olivan/Documents/Eugenialazaro.com/pythonProject/src/main.py"


import PySimpleGUI as sg
import os.path
import ImageResizer as ir

def Warning (msg):
    sg.Popup(msg, keep_on_top=True)

if __name__ == '__main__':

    layout0 = [
        [
            sg.Text("SELECCIONE OPCIÓN", pad = (75, 4)),
        ],
        [
            sg.Button("Resize Images", pad = (100, 4)),
        ]
    ]

    listaFicherosColumna = [
        [
          sg.Button("Atrás"),
        ],
        [
            sg.Text("Carpeta:"),
            sg.In(size=(90, 1), enable_events=True, key="-FOLDER1-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(800, 20), key="-FILE LIST-"
            )
        ],
        [sg.Button('Convierte la carpeta completa'), ],
    ]

    layout1 = [ [sg.Column(listaFicherosColumna),]]

    layout = [
        [
            sg.Column(layout0, key='-LAYOUT0-'),
            sg.Column(layout1, visible=False, key='-LAYOUT1-'),
        ]
    ]

    window = sg.Window("Eugenia Pintura - Subir Imagenes", layout,
                       icon=r'C:\Users\Juane Olivan\Documents\Eugenialazaro.com\repositorioImagenes\sol.ico', size=(320, 200), location = (400,75))

    layoutActual = "LAYOUT0"
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == 'Resize Images':
            window[f'-LAYOUT0-'].update(visible=False)
            layoutActual = "LAYOUT1"
            window.size = (800,500)
            window[f'-LAYOUT1-'].update(visible=True)

        elif event == "Atrás":
            window[f'-'+layoutActual+'-'].update(visible=False)
            layoutActual = "LAYOUT0"
            window.size = (320, 200)
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
                    and f.lower().endswith((".jpeg", ".gif", ".jpg", ".png"))
            ]
            window["-FILE LIST-"].update(fnames)

        if event == 'Convierte la carpeta completa':
            try:
                ir.imageResizerFolder(values["-FOLDER1-"], "")
            except NameError:
                Warning("Error: No se ha seleccionado ninguna carpeta a procesar")


        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            clicked = sg.PopupOKCancel("Quieres procesar la imagen "+values["-FILE LIST-"][0])
            if clicked == 'OK':
                try:
                    ir.imageResizerFile(values["-FILE LIST-"][0], values["-FOLDER1-"])
                except NameError:
                    Warning("Error: No se ha seleccionado ninguna foto a convertir")
            elif clicked == 'Cancel':
                pass
            elif clicked == None:
                pass

    window.close()
