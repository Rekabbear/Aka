import tkinter as tk
from tkinter import filedialog as tkDia
import os

Title = "HTML Creater"
PathText = "github URL (e.g. https://github.com/Sanno/Folder/blob/main/Model.glb)"
ProjectText = "Project Name"
NameText = "Html-File Name"
FolderText = "File location"
BrowseText = "Browse"

ButtonText = "Create"
TITLE = "Sanno 3D-viewer"
TXT = "View in AR"

Folder = os.path.dirname(__file__)

root = tk.Tk()
root.title(Title)
root.rowconfigure([0,10],minsize = 5)
root.columnconfigure([0,10],minsize = 70)

NameVar = tk.StringVar(root)

PathVar = tk.StringVar(root)

ProjectVar = tk.StringVar(root)
# Export Text File
def File(event):
    Path = PathVar.get()
    Path = Path.replace('github','raw.githubusercontent')
    Path = Path.replace('/blob/','/')

    Project = ProjectVar.get()

    Name = NameVar.get()
    FileName = ''.join([Folder,"\\", Name, ".html"])
    Txt = open(FileName,'w')
    Txt.write('''<!DOCTYPE html>
        <html lang="en">
          <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">	
                
                <title>'''+TITLE+'''</title>
          </head>
          <body>
                <img src="https://raw.githubusercontent.com/Rekrabbear/Aka/main/Sanno3D.png" alt="SANNO GROUP" height="100">
                <p>Project: '''+Project+'''</p>
                <br>
                
                <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.1.1/model-viewer.min.js"></script>
                <style>
                        model-viewer {
                                width: 1000px;
                                height: 1000px;
                        }
                </style>
                <model-viewer 
                        id="model-viewer"
                        alt="'''+Project+'''" 
                        src="'''+Path+'''" 
                        shadow-intensity="1" 
                        ar ar-modes="scene-viewer webxr"
                        camera-controls touch-action="pan-y">
                
                        <div id="error"
                        class="hide">
                        AR is not supported on Device
                        </div>

                        <button slot="ar-button" style="background-color: white; border-radius: 5px; border: solid; position: absolute; top: 16px; left: 16px; ">
                                '''+TXT+'''
                        </button>
                        
                </model-viewer>
                <script>
                        document.querySelector("#model-viewer").addEventListener('ar-status', (event) => {
                                if(event.detail.status === 'failed'){
                                        const error = document.querySelector("#error");
                                        error.classList.remove('hide');
                                        error.addEventListener('transitionend',(event) => {
                                                error.classList.add('hide');
                                        });
                                }
                        });
                </script>
                <style>
                        #error {
                                background-color: #ffffffdd;
                                border-radius: 16px;
                                padding: 16px;
                                position: absolute;
                                left: 50%;
                                top: 50%;
                                transform: translate3d(-50%, -50%, 0);
                                transition: opacity 0.3s;
                        }
                        #error.hide {
                                opacity: 0;
                                visibility: hidden;
                                transition: visibility 2s, opacity 1s 1s;
                        }
                </style>
          </body>
        </html>''')
    root.destroy()

def Browsing(event):
    global Folder
    Folder = tkDia.askdirectory()
    FolderEntry["text"] = Folder
    
# Add Buttons & Labels
#region

BrowseButton = tk.Button(root, text = BrowseText, command = Browsing)
BrowseButton["width"] = "12"
BrowseButton.grid(row=3, column=2, sticky="w")
BrowseButton.bind('<Return>', Browsing)
BrowseButton.bind('<ButtonRelease-1>', Browsing)

FileButton = tk.Button(root, text = ButtonText)
FileButton["width"] = "12"
FileButton.grid(row=4, column=0)
FileButton.bind('<Return>', File)
FileButton.bind('<Button-1>', File)

PathEntry = tk.Entry(root)
PathEntry["textvariable"] = PathVar
PathEntry.grid(row=0, column=0)

PathLabel = tk.Label(root)
PathLabel["text"] = PathText
PathLabel.grid(row=0, column=1,columnspan=20)

ProjectEntry =tk.Entry(root)
ProjectEntry["textvariable"] = ProjectVar
ProjectEntry.grid(row=1, column=0)

ProjectLabel = tk.Label(root)
ProjectLabel["text"] = ProjectText
ProjectLabel.grid(row=1, column=1, sticky="w")

NameEntry = tk.Entry(root)
NameEntry["textvariable"] = NameVar
NameEntry.grid(row=2, column=0)

NameLabel = tk.Label(root)
NameLabel["text"] = NameText
NameLabel.grid(row=2, column=1, sticky="w")

FolderEntry = tk.Label(root)
FolderEntry["text"] = Folder
FolderEntry["width"] = 17
FolderEntry["relief"] = "sunken"
FolderEntry["bg"] = "white"
FolderEntry["anchor"] = "e"
FolderEntry.grid(row=3, column=0)

FolderLabel = tk.Label(root)
FolderLabel["text"] = FolderText
FolderLabel.grid(row=3, column=1, sticky="w")

#endregion

root.mainloop()
