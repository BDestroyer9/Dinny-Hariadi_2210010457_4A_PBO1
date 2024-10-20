import PySimpleGUI as sg
sg.theme("DarkGrey9")
sg.theme_text_color("#F0FFFF")

susunan=[[sg.Text("UNISKA MAB", font=("Arial", 20,"bold","italic"), text_color=("#FFCC00"))],
        [sg.Text("FAKULTAS TEKNIK INFORMATIKA")]]


window = sg.Window(title="New Icon",
                layout=susunan,
                element_justification= "center",
                icon="favicon.ico",
                resizable=True,
                size=(500,200))
window()
window.close()