class Pos:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Addition de deux Pos"""
        return Pos(self.x + other.x, self.y+other.y)
    