import PySimpleGUI as sg
import os.path
import ImageResizer as ir


file_list_column = [
    [
        sg.Text("Carpeta:"),
        sg.In(size=(90, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(90, 20), key="-FILE LIST-"
        )
    ],
    [sg.Button('Convierte la carpeta completa'), ],
]

# image_viewer_column = [
#     [sg.Text("Choose an image from list on left:")],
#     [sg.Text(size=(40, 1), key="-TOUT-")],
#     [sg.Image(key="-IMAGE-")],
# ]

layout = [
    [
        sg.Column(file_list_column),
        # sg.VSeperator(),
        # sg.Column(image_viewer_column),

    ]
]

window = sg.Window("Prepararador de imagenes BIG/SMALL", layout)

while True:
    print = sg.Print
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        print("folder")
        folder = values["-FOLDER-"]
        try:
            print("try")
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            print("except")
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".jpeg", ".gif"))
        ]
        for x in fnames:
            print(x)
        window["-FILE LIST-"].update(fnames)

    if event == 'Convierte la carpeta completa':
        print("go")
    # elif event == "-FILE LIST-":  # A file was chosen from the listbox
    #     try:
    #         filename = os.path.join(
    #             values["-FOLDER-"], values["-FILE LIST-"][0]
    #         )
    #         window["-TOUT-"].update(filename)
    #         window["-IMAGE-"].update(filename=filename)
    #     except:
    #         pass

window.close()
