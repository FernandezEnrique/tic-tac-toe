import PIL
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

def show_message(caption, msg, btn):
    win = Tk()
    win.title(caption)
    win.geometry(f"300x150")
    #win.iconbitmap('icono.ico') hay que convertir el archivo
    win.config(bg="cornsilk4") 
    win.resizable(0,0)

    font_winner = font.Font(family='Tahoma', size=16)
    font_exit = font.Font(family='Comic Sans MS', size=8)

    Label(win, text=msg, font=font_winner, bg="cornsilk3", fg="black").pack(pady=20)
    exit_button = Button(win, text=btn, font=font_exit, bg="cornsilk3", fg="black", command=win.destroy, width=25)
    exit_button.pack(pady=20)
    win.mainloop()

def menu(caption, msg, btn1, btn2):
    win = Tk()
    win.title(caption)
    win.geometry(f"450x550")
    win.config(bg="cornsilk4") 
    win.resizable(0,0)

    
    image = Image.open("img/readme/game-img.png")
    image = image.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    
    def local():
        win.destroy()
        return "Local"


    def machine():
        win.destroy()
        return "Machine"

    font_button = font.Font(family='Tahoma', size=16)

    Label(win, text=msg, font=font_button, bg="cornsilk3", fg="black").pack(pady=20)
    local_button = Button(win, text = btn1, font = font_button, bg="cornsilk3", fg="black", command=local).pack(pady=20)
    machine_button = Button(win, text = btn2, font = font_button, bg="cornsilk3", fg="black", command = machine).pack(pady=20)
    lbl_img = Label(win, image = img)
    lbl_img.pack()

    
    win.mainloop()