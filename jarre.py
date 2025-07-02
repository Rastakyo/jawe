class Jarre:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.state = "hidden"  # peut être: hidden, beer, serpent, bonus, malus

    def set_state(self, state):
        self.state = state
