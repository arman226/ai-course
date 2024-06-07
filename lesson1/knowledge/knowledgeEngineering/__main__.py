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

# Initialize the game
game = ClueGame()

# Add clues obtained during the game
game.add_clue('Miss Scarlett', 'Candlestick', 'Ballroom', 'Player 1')
game.add_clue('Colonel Mustard', 'Knife', 'Library', 'Player 2')
game.add_clue('Mrs. White', 'Rope', 'Billiard Room', 'Player 3')
game.add_clue('Mr. Green', 'Revolver', 'Conservatory', 'Player 4')
game.add_clue('Mrs. Peacock', 'Wrench', 'Dining Room', 'Player 5')

# Make deductions based on the clues
game.make_deductions()

# Examine remaining possibilities to determine the final answer
# For example, print the remaining possibilities
remaining_possibilities = []
for suspect in game.suspects:
    for weapon in game.weapons:
        for room in game.rooms:
            if not game.kb[(suspect, weapon, room)]:
                remaining_possibilities.append((suspect, weapon, room))

if len(remaining_possibilities) == 1:
    final_answer = remaining_possibilities[0]
    print("Final Answer:", final_answer)
else:
    print(f"Multiple possibilities remain. Further deductions needed.{len(remaining_possibilities)}")