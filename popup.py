from tkinter import *

def show_message(caption, msg, btn):
    win = Tk()
    win.title(caption)
    win.geometry(f"300x150")
    Label(win, text=msg, font=('Arial 16')).pack(pady=20)
    exit_button = Button(win, text=btn, command=win.destroy, width=25)
    exit_button.pack(pady=20)
    win.mainloop()