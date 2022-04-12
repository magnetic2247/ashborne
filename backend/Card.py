class Card:
    # Constructor
    def __init__(self, value, sign):
        # Check Arguments
        if sign.lower() not in ["hearts", "diamonds", "clubs", "spades"]: raise ValueError("Invalid card sign")
        if not (1 < value < 16): raise ValueError("Invalid card value")
            
        # Store Attributes
        self.value = value
        self.sign = sign

    # Calculate Card ID (number n in sorted deck, from 0 to 51)
    def id(self):
        return ["hearts", "clubs", "diamonds", "spades"].index(self.sign) * 13 + self.value - 2
    
    # Convert to String
    def __str__(self):
        # If Value is bigger than 10, card has a name (valet, dame, roi, as)
        if self.value > 10:
            # one-liner to get card name based on value
            cardname = ["prince","queen","king","ace"][self.value-11]
            return f"{cardname} of {self.sign}"
        
        # Otherwise, the card is named by it's value
        return f"{self.value} of {self.sign}"

    
    # Compare
    def __lt__(self, other):
        if type(other) != Card: raise ValueError("Cannot compare card to", type(other))
        return self.value < other.value
    
    # Equality
    def __eq__(self, other):
        if type(other) != Card: raise ValueError("Cannot compare card to", type(other))
        return self.value == other.value
