import PySimpleGUI as sg
from extract import extract_archive


sg.theme("LightPurple")
label = sg.Text("Select archive:")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key='file')

label2 = sg.Text("Select destination:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key='folder')
extract = sg.Button("Extract")

window = sg.Window("ARCHIVE EXTRACTOR", layout= [[label, input1 , button1],
                                        [label2, input2, button2],
                                        [extract]],
                                        font=("Helvetica", 20))
while True:
    event, values = window.read()
    filepath = values['file']
    dest_dir = values['folder']
    extract_archive(filepath, dest_dir)
    sg.Popup("Extraction completed")
    window.close()