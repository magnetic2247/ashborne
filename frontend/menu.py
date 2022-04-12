#!/usr/bin/python
from tkinter import *
import subprocess

# Window Size
window_width = 810
window_height = 477

# Main Window
ws = Tk()
ws.title("Ashborne")
ws.geometry(f"{window_width}x{window_height}")
ws.resizable(0,0)

# Background Image
canvas = Canvas(ws, width=window_width, height=window_height)
canvas.pack(expand=YES, fill=BOTH)
background = PhotoImage(file="assets/MenuBackground.png")
canvas.create_image(0, 0, image=background, anchor=NW)

# Spinbox for Round Count
spinny_boi = Spinbox(ws, from_=5, to=100, width=35)
spinny_boi.place(x=276, y=232)

# Play Button
play_button = Button(canvas, text="Play", width=34, bd=0)
play_button.place(x=275, y=200)


# Button Clicked Event
def button_clicked(event):
    global play_button
    subprocess.run(["python", "frontend/game.py", spinny_boi.get()]) # This is hacky at best and should never be used. I'm tired.

# Bind Events
play_button.bind('<Button-1>', button_clicked)
# Main Loop
ws.mainloop()
