#!/usr/bin/python
from tkinter import *
import tkinter.font
import sys
sys.path.insert(1, 'backend/')
import Game

# Process Arguments
print(sys.argv, len(sys.argv))
if len(sys.argv) == 2: r = int(sys.argv[1])
else: r = 10

# Game Object
game = Game.Bataille(rounds=r)


# Window Size
window_width = 1323
window_height = 750


# Main Window
ws = Tk()
ws.title("Ashborne")
ws.geometry(f"{window_width}x{window_height}")
ws.resizable(0,0)


# Background Image
canvas = Canvas(ws, width=window_width, height=window_height)
canvas.pack(expand=YES, fill=BOTH)
background = PhotoImage(file="assets/ArenaBackground.png")
canvas.create_image(0, 0, image=background, anchor=NW)


# Player Cards
image1 = PhotoImage(file=f"assets/cards/{game.player1.top().id()}.png").zoom(4)
image2 = PhotoImage(file=f"assets/cards/{game.player2.top().id()}.png").zoom(4)
card1 = canvas.create_image(235, 275, image=image1, anchor=NW)
card2 = canvas.create_image(948, 275, image=image2, anchor=NW)


# Player Score 
player1 = PhotoImage(file="assets/cards/player1.png").zoom(2)
score1 = canvas.create_text(93, 20, text=f"{len(game.player1)}", fill="white", font='Helvetica 15 bold')
canvas.create_image(5, 5, image=player1, anchor=NW)

player2 = PhotoImage(file="assets/cards/player2.png").zoom(2)
score2 = canvas.create_text(1230, 20, text=f"{len(game.player2)}", fill="white", font='Helvetica 15 bold')
canvas.create_image(1248, 5, image=player2, anchor=NW)

# Additional Text
roundcount = canvas.create_text(660, 50, text=f"ROUND {game.round_count}", fill="white", font='Helvetica 20 bold')
undertext = canvas.create_text(670, 700, text="PRESS SPACE", fill="white", font='Helvetica 20 bold')


# Keyboard Event, play round and update score
def keyev(event):
    # Access required widgets
    global game, canvas, card1, card2, score1, score2, roundcount

    # Exit if Game is finished
    if game.finished: sys.exit()

    # Play One Round
    game.play()

    # If Game is Finished, Show Winner
    if game.finished:
        # Determine Winner
        if len(game.player1) == len(game.player2): msg = "TIE"
        elif len (game.player1) > len(game.player2): msg = "PLAYER 2 WON!"
        else: msg = "PLAYER 1 WON!"

        # Show Winner
        canvas.delete(roundcount)
        roundcount = canvas.create_text(660, 50, text=msg, fill="white", font='Helvetica 20 bold')
        
        # End function
        return

    # Delete old canvas elements
    canvas.delete(card1, card2, score1, score2, roundcount)

    # Add New Cards
    ws.image1 = image1 = PhotoImage(file=f"assets/cards/{game.player1.top().id()}.png").zoom(4)
    ws.image2 = image2 = PhotoImage(file=f"assets/cards/{game.player2.top().id()}.png").zoom(4)
    card1 = canvas.create_image(235, 275, image=image1, anchor=NW)
    card2 = canvas.create_image(948, 275, image=image2, anchor=NW)

    # Add New Score
    score1 = canvas.create_text(93, 20, text=f"{len(game.player1)}", fill="white", font='Helvetica 15 bold')
    score2 = canvas.create_text(1230, 20, text=f"{len(game.player2)}", fill="white", font='Helvetica 15 bold')

    # Add new Round Count
    roundcount = canvas.create_text(660, 50, text=f"ROUND {game.round_count}", fill="white", font='Helvetica 20 bold')

# Bind Events
ws.bind("<space>", keyev)
# Main Loop
ws.mainloop()
