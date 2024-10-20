import PySimpleGUI as sg
sg.theme("DarkGrey9")
sg.theme_text_color("#F0FFFF")

susunan=[[sg.VPush(),
            sg.Text("UNISKA MAB", font=("Arial", 20,"bold","italic"), text_color=("#FFCC00")),
            sg.Push()],
        [sg.Push(),      
            sg.Text("FAKULTAS TEKNIK INFORMATIKA"),
            sg.Push()],
        [sg.VPush()]
        ]

window = sg.Window(title="Elemen Text",
                layout=susunan,
                size=(500,200),
                font=("Comic", 18))
window()
window.close()