import tkinter as tk
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re

window = tk.Tk()
textbox = tk.Text()

menubar = tk.Menu()

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

def initMenu():
    filesubmenu = tk.Menu(tearoff=0)
    filesubmenu.add_separator()
    menubar.add_cascade(label='File', menu=filesubmenu)

def configureWindow():
    window.config(menu=menubar)
    window.title("pyedit")

def main():
    initMenu()
    initSyntaxHighlighting()
    configureWindow()
    textbox.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
else:
    print("You shouldn't import this file!")
    raise SystemExit()