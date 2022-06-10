import PySimpleGUI as sg
import os.path
import ImageResizer as ir

def Warning (msg):
    sg.Popup(msg, keep_on_top=True)

file_list_column = [
    [
        sg.Text("Carpeta:"),
        sg.In(size=(90, 1), enable_events=True, key="-FOLDER1-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(90, 20), key="-FILE LIST-"
        )
    ],
    [sg.Button('Convierte la carpeta completa'), ],
]

layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("Prepararador de imagenes BIG/SMALL",  layout, icon=r'C:\Users\Juane Olivan\Documents\Eugenialazaro.com\repositorioImagenes\sol.ico')

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

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
