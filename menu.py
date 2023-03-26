import PIL
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

class Menu:
    def __init__(self, caption, msg, btn1, btn2):
        self.win = Tk()
        self.win.title(caption)
        self.win.geometry(f"450x550")
        self.win.config(bg="cornsilk4") 
        self.win.resizable(0,0)
        self.selection = None
        self.win.iconbitmap('img/icono.ico')

        
        image = Image.open("img/game-img.png")
        image = image.resize((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)

        font_button = font.Font(family='Tahoma', size=16)

        Label(self.win, text=msg, font=font_button, bg="cornsilk3", fg="black").pack(pady=20)
        local_button = Button(self.win, text = btn1, font = font_button, bg="cornsilk3", fg="black", command=self.local).pack(pady=20)
        machine_button = Button(self.win, text = btn2, font = font_button, bg="cornsilk3", fg="black", command = self.machine).pack(pady=20)
        lbl_img = Label(self.win, image = img)
        lbl_img.pack()

        
        self.win.mainloop()
    
    def local(self):
        self.selection = "Local"
        self.win.destroy()
        return "Local"


    def machine(self):
        self.selection = "Machine"
        self.win.destroy()
        return "Machine"