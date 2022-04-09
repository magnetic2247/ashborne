"""
Bataile v0.1
Author: Polis Minus
License: GPL
Bataille Game backend
"""

from Queue import Queue 
from Card import Card 
import random 


class Bataille:
    # Constructor
    def __init__(self, autoplay=False, rounds=10, verbose=False):
        # Set base card pack
        self.base_cards = Queue(52)
        for sign in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(2,15):
                self.base_cards.push(Card(value, sign))

        # Player Decks
        self.player1, self.player2 = Queue(), Queue()

        # Shuffle Cards 
        self.shuffle()

        # Start Game, unless specified otherwise
        if autoplay: self.play(rounds, verbose)


    # Shuffle Cards 
    def shuffle(self):
        # Shuffle Base Cards
        random.shuffle(self.base_cards.file)
        # Distribute first cards to each player
        for i in range(11): self.player1.push(self.base_cards.file[i])
        for i in range(12,23): self.player2.push(self.base_cards.file[i])


    # Play n rounds
    def play(self, rounds=1, verbose=False):
        # Print Game State 
        if verbose:
            print("Player 1 has:", [str(a) for a in self.player1.file],"\nPlayer 2 has:", [str(a) for a in self.player2.file], "\n\n")

        # Set amount of rounds
        for round in range(rounds):
            print("Round",round,end=": ")
            # Player 1 Won
            if self.player1.top() > self.player2.top():
                self.player2.push(self.player1.pop())
                self.player2.push(self.player2.pop())
                print("player 1")

            # Player 2 Won
            elif self.player2.top() > self.player1.top():
                self.player1.push(self.player2.pop())
                self.player1.push(self.player1.pop())
                print("player 2")

            # Draw 
            else:
                self.player1.push(self.player1.pop())
                self.player2.push(self.player2.pop())
                print("draw")

        # Print Game State 
        if verbose:
            print("Player", 1 if len(self.player1.file)<len(self.player2.file) else 2, "won")
