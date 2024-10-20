import PySimpleGUI as sg
window = sg.Window(title="Identitas Diri Mahasiswa",
                layout=[
                    [sg.Text("NPM   : 2210010457")],
                    [sg.Text("NAMA  : DINNY HARIADI")],
                    [sg.Text("KELAS : FTI 5A NREG BJM")],
                    [sg.Text("MATKUL: PEMOGRAMAN VISUAL 3")],
                ],
                        size=(400,200))
window()
window.close