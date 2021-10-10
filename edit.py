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

def initTextBox():
    initSyntaxHighlighting()
    textbox.bind("<Key>",fileChanged)

def initMenu():
    filesubmenu = tk.Menu(tearoff=0)
    filesubmenu.add_command(label="New")
    filesubmenu.add_command(label="Open", command=openDialog)
    filesubmenu.add_command(label="Save")
    filesubmenu.add_command(label="Save As")
    filesubmenu.add_separator()
    filesubmenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label='File', menu=filesubmenu)

def fileChanged(key):
    saved = False
    if currentFile != "":
        window.title(f"pyedit: {currentFile}*")
    else:
        window.title("pyedit*")

def configureWindow():
    window.config(menu=menubar)
    window.title("pyedit")

def changeCurrentFile(newFile):
    global currentFile
    currentFile = newFile
    if currentFile != "":
        window.title(f"pyedit: {currentFile}")
    else:
        window.title("pyedit")

def openDialog():
    filepath = askopenfilename(filetypes=[("Python Scripts", "*.py")])
    try:
        with open(filepath, 'r') as f:
            textbox.delete('1.0', tk.END)
            textbox.insert('1.0', f.read())
            changeCurrentFile(filepath)
    except:
        pass

def main():
    initMenu()
    initTextBox()
    configureWindow()
    textbox.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
else:
    print("You shouldn't import this file!")
    raise SystemExit()