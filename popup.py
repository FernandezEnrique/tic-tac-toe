import PIL
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

def show_message(caption, msg, btn):
    win = Tk()
    win.title(caption)
    win.geometry(f"300x150")
    win.iconbitmap('img/icono.ico')
    win.config(bg="cornsilk4") 
    win.resizable(0,0)

    font_winner = font.Font(family='Tahoma', size=16)
    font_exit = font.Font(family='Comic Sans MS', size=8)

    Label(win, text=msg, font=font_winner, bg="cornsilk3", fg="black").pack(pady=20)
    exit_button = Button(win, text=btn, font=font_exit, bg="cornsilk3", fg="black", command=win.destroy, width=25)
    exit_button.pack(pady=20)
    win.mainloop()