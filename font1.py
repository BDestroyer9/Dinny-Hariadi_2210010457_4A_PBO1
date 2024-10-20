import PySimpleGUI as sg
sg.theme("DarkGrey9")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="Identitas Diri Mahasiswa",
                layout=[
                    [sg.Text("Universitas Islam Kalimantan MAB", font=("Arial", 20,"bold"))],
                    [sg.Text("NPM   : 2210010457")],
                    [sg.Text("NAMA  : DINNY HARIADI")],
                    [sg.Text("KELAS : FTI 5A NREG BJM")],
                ],
                    size=(500,200),
                    font=("Comic", 18))
window()
window.close()