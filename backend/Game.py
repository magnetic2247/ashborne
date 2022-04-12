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
    def __init__(self, autoplay=False, rounds=10):
        # Set base card pack
        self.base_cards = Queue(52)
        for sign in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(2,15):
                self.base_cards.push(Card(value, sign))

        # Player Decks
        self.player1, self.player2 = Queue(), Queue()

        # Shuffle Cards 
        self.shuffle()

        # Round Count, Total num of rounds and Whether Game is Finished or not
        self.round_count = 0
        self.rounds = rounds
        self.finished = False

        # Start Game, unless specified otherwise
        if autoplay: self.play(rounds)


    # Shuffle Cards 
    def shuffle(self):
        # Shuffle Base Cards
        random.shuffle(self.base_cards.file)

        # Distribute first cards to each player
        for i in range(11): self.player1.push(self.base_cards.file[i])
        for i in range(12,23): self.player2.push(self.base_cards.file[i])


    # Play n rounds
    def play(self, rounds=1):
        # Loop n times (n=rounds)
        for round in range(rounds):
            # Update Round Count
            self.round_count += 1

            # Player 1 Won
            if self.player1.top() > self.player2.top():
                self.player2.push(self.player1.pop())
                self.player2.push(self.player2.pop())

            # Player 2 Won
            elif self.player2.top() > self.player1.top():
                self.player1.push(self.player2.pop())
                self.player1.push(self.player1.pop())

            # Draw 
            else:
                self.player1.push(self.player1.pop())
                self.player2.push(self.player2.pop())

        # Check if game is finished
        if self.round_count == self.rounds: self.finished = True
