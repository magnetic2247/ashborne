from tkinter import *
import tkinter.font

# Window Size
window_width = 810
window_height = 477

# Main Window
ws = Tk()
ws.title("Ashborne")
ws.geometry(f"{window_width}x{window_height}")
ws.resizable(0,0)


# Background Image
#l = Label(ws, image=background)
l = Canvas(ws, width=window_width, height=window_height)
l.pack(expand=YES, fill=BOTH)
background = PhotoImage(file="assets/Menu_BG.png")
l.create_image(0, 0, image=background, anchor=NW)

# Button
play_button = Button(l, text="Play", width=34, bd=0)
play_button.place(y=100)

ws.mainloop()
