class ClueGame:
    def __init__(self):
        self.suspects = ['Miss Scarlett', 'Colonel Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Professor Plum']
        self.weapons = ['Candlestick', 'Knife', 'Lead Pipe', 'Revolver', 'Rope', 'Wrench']
        self.rooms = ['Kitchen', 'Ballroom', 'Conservatory', 'Dining Room', 'Billiard Room', 'Library', 'Lounge', 'Hall', 'Study']

        self.players = {}  # Placeholder for player information

        # Knowledge base
        self.kb = {}

        # Initialize knowledge base with all possible combinations of suspects, weapons, and rooms
        for suspect in self.suspects:
            for weapon in self.weapons:
                for room in self.rooms:
                    self.kb[(suspect, weapon, room)] = False

    def add_clue(self, suspect, weapon, room, player):
        # Mark the given combination as true in the knowledge base
        self.kb[(suspect, weapon, room)] = True

        # Update player's knowledge base with the new clue
        if player not in self.players:
            self.players[player] = set()
        self.players[player].add((suspect, weapon, room))

    def make_deductions(self):
        # Make deductions based on the knowledge base
        for player, knowledge in self.players.items():
            for suspect in self.suspects:
                for weapon in self.weapons:
                    for room in self.rooms:
                        # If the combination is not in the player's knowledge and not marked as True in the knowledge base, it must be False
                        if (suspect, weapon, room) not in knowledge and not self.kb[(suspect, weapon, room)]:
                            print(f"{player} deduces that {suspect} did not commit the murder with the {weapon} in the {room}.")

# Example usage:
game = ClueGame()
game.add_clue('Miss Scarlett', 'Candlestick', 'Ballroom', 'Player 1')
game.add_clue('Colonel Mustard', 'Knife', 'Library', 'Player 2')

# Make deductions
game.make_deductions()