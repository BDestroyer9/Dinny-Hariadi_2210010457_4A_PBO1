import PySimpleGUI as sg
sg.theme("DarkGrey9")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="Any where Button ",
                layout=[[sg.Text("Any where Button")],
                        [sg.Button("Liburan")],
                        [sg.Button("Hiburan")]],
                element_justification= "left",
                icon="favicon.ico",
                resizable=True,
                size=(500,200))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()