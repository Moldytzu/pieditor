import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re

window = tk.Tk()
textbox = tk.Text()
menubar = tk.Menu()

currentFile = ""

saved = True

def initSyntaxHighlighting():
    cdg = ic.ColorDelegator()
    cdg.prog = re.compile(r'\b(?P<DEFAULT>tkinter)\b|' + ic.make_pat(), re.S)
    cdg.idprog = re.compile(r'\s+(\w+)', re.S)

    cdg.tagdefs['DEFAULT'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}
    cdg.tagdefs['COMMENT'] = {'foreground': '#008022', 'background': '#FFFFFF'}
    cdg.tagdefs['KEYWORD'] = {'foreground': '#003bff', 'background': '#FFFFFF'}
    cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
    cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
    cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

    ip.Percolator(textbox).insertfilter(cdg)

def updateTitle():
    if not saved:
        if currentFile != "":
            window.title(f"PIeditor: {currentFile}*")
        else:
            window.title("PIeditor*")
    else:
        if currentFile != "":
            window.title(f"PIeditor: {currentFile}")
        else:
            window.title("PIeditor")

def initTextBox():
    initSyntaxHighlighting()
    textbox.bind("<Key>",fileChanged)

def initMenu():
    filesubmenu = tk.Menu(tearoff=0)
    filesubmenu.add_command(label="New", command=new)
    filesubmenu.add_command(label="Open", command=openDialog)
    filesubmenu.add_command(label="Save", command=saveDialog)
    filesubmenu.add_command(label="Save As", command=saveasDialog)
    filesubmenu.add_separator()
    filesubmenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label='File', menu=filesubmenu)

def fileChanged(key):
    global saved
    saved = False
    updateTitle()

def configureWindow():
    window.config(menu=menubar)
    window.title("PIeditor")

def changeCurrentFile(newFile):
    global currentFile
    currentFile = newFile
    updateTitle()

def openDialog():
    filepath = askopenfilename(filetypes=[("Python Scripts", "*.py")])
    try:
        with open(filepath, 'r') as f:
            textbox.delete('1.0', tk.END)
            textbox.insert('1.0', f.read())
            changeCurrentFile(filepath)
    except:
        pass

def saveDialog():
    global saved
    if currentFile == "":
        saveasDialog()
    else:
        saved = True
        updateTitle()
        with open(currentFile, "w") as f:
            f.write(textbox.get("1.0", tk.END))
            

def saveasDialog():
    global saved
    filepath = asksaveasfilename(filetypes=[("Python Scripts", "*.py")])
    try:
        saved = True
        updateTitle()
        changeCurrentFile(filepath)
        with open(filepath, "w") as f:
            f.write(textbox.get("1.0", tk.END))
    except:
        pass

def new():
    textbox.delete('1.0', tk.END)
    saved = True
    changeCurrentFile("")

def main():
    initMenu()
    initTextBox()
    configureWindow()
    textbox.pack(fill=tk.BOTH, expand=1)
    window.mainloop()

if __name__ == "__main__":
    main()
else:
    print("You shouldn't import this file!")
    raise SystemExit()
