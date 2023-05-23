import tkinter as tk

Title = "HTML Creater"
PathText = "insert github URL (e.g. https://github.com/Sanno/Folder/blob/main/Model.glb)"
NameText = "insert File Name"

ButtonText = "Create"
TXT = "Display 3D-Model"

root = tk.Tk()
root.title(Title)
root.rowconfigure([0,10],minsize = 5)
root.columnconfigure([0,10],minsize = 70)

NameVar = tk.StringVar(root)

PathVar = tk.StringVar(root)
# Export Text File
def File():
    
    Path = PathVar.get()
    Path = Path.replace('github','raw.githubusercontent')
    Path = Path.replace('/blob/','/')

    Name = NameVar.get()
    FileName = ''.join(["C:\\Users\\HP\\Desktop\\", Name, ".html"])
    Txt = open(FileName,'w')
    Txt.write('<a href="intent://arvr.google.com/scene-viewer/1.0?file='+Path+'#Intent;scheme=https;package=com.google.android.googlequicksearchbox;action=android.intent.action.VIEW;S.browser_fallback_url=https://developers.google.com/ar;end;">'+TXT+'</a>')      

# Add Buttons & Labels
#region


FileButton = tk.Button(root, text = ButtonText, command = File)
FileButton["width"] = "12"
FileButton.grid(row=2, column=0)

PathEntry = tk.Entry(root)
PathEntry["textvariable"] = PathVar
PathEntry.grid(row=0, column=0)

PathLabel = tk.Label(root)
PathLabel["text"] = PathText
PathLabel.grid(row=0, column=1)

NameEntry = tk.Entry(root)
NameEntry["textvariable"] = NameVar
NameEntry.grid(row=1, column=0)

NameLabel = tk.Label(root)
NameLabel["text"] = NameText
NameLabel.grid(row=1, column=1, sticky="w")
#endregion

root.mainloop()
