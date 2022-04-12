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
canvas = Canvas(ws, width=window_width, height=window_height)
canvas.pack(expand=YES, fill=BOTH)
background = PhotoImage(file="assets/MenuBackground.png")
canvas.create_image(0, 0, image=background, anchor=NW)

# Play Button
play_button = Button(canvas, text="Play", width=34, bd=0)
play_button.place(x=275, y=200)

# Main Loop
ws.mainloop()
