import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import askopenfile
import base64

#Create app window
def create_app_window():
        global top
        global root
        img=b'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'
        root= tk.Tk()
        top= root
        top.geometry("600x450+468+138")
        top.resizable(0,0)
        top.title("Base64 encode")
        favicon=tk.PhotoImage(data=img) 
        root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.918, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)
        textbox.configure(state=DISABLED)

#Open File
def open_file():
    global iconfile
    data=[('PNG', '*.png')]
    iconfile=askopenfile(mode='rb',filetypes=data)
    if str(iconfile)!='None':
            encode()

#encode
def encode():
    icondata = iconfile.read()
    icondata = base64.b64encode(icondata)
    icondatastring=str(icondata)
    textbox.configure(state=NORMAL)
    textbox.delete(1.0,END)
    textbox.insert(INSERT,icondatastring)
    textbox.configure(state=DISABLED)

#Copy Code
def copy_code():
    textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Copy>>"))

#Quit
def QuitApp():
    top.destroy()

#menu
def create_menu():
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="Edit")
    sub_menu.add_command(compound="left", label="Open", command=open_file)
    sub_menu.add_command(compound="left",label="Copy", command=copy_code)
    menubar.add_command(compound="left",label="Quit", command=QuitApp)

#contextmenu
def context_menu(event):
        try:
                menucopy.tk_popup(event.x_root, event.y_root)
        finally:
                menucopy.grab_release()
def create_context_menu():
        global menucopy
        root.bind("<Button-3>", context_menu)
        menucopy = Menu(root, tearoff = 0)
        menucopy.add_command(label="Copy", command=copy_code)

#main procedure
def main():
    create_app_window()
    create_textbox()
    create_menu()
    create_context_menu()


main()
root.mainloop()
