import PySimpleGUI as sg
sg.theme("DarkGrey9")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="FTI UNISKA",
                layout=[
                    [sg.Text("Universitas Islam Kalimantan MAB", font=("Arial", 20,"bold","italic"), text_color="#FFCC00")],
                    [sg.Text("FAKULTAS TEKNIK INFORMATIKA", justification="left")],
                ],
                    size=(500,200),
                    font=("Comic", 18))
window()
window.close()