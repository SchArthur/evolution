import pygame

maximum_energy = 1500

class foodMatrix:
    def __init__(self, matrix_height, matrix_width, surface, cell_size) -> None:
        self.surface = surface
        self.cell_size = cell_size

        self.matrix = []
        for y in range(matrix_height):
            line = []
            self.matrix.append(line)
            for x in range(matrix_width):
                cell = []
                self.matrix[y].append(cell)
                self.matrix[y][x] = []

    def draw(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] != []: 
                    self.matrix[y][x].draw()

    def addFood(self, x, y):
        pos = pygame.Vector2(x,y)
        if self.matrix[y][x] == []:
            self.matrix[y][x] = newFood(self.surface, pos, self.cell_size)

    def eatFood(self, x, y) -> int:
        if self.matrix[y][x] != []: 
            self.matrix[y][x] = []
            return 1
        else:
            return 0

    def printMatrix(self):
        print(self.matrix)

class newFood:
    def __init__(self, surface, pos : pygame.Vector2, cell_size) -> None:
        self.surface = surface
        self.cell_size = cell_size
        self.pos = pos

    def draw(self):
        top_left = self.pos * self.cell_size
        size = (self.cell_size, self.cell_size)
        rect = pygame.rect.Rect(top_left, size)
        pygame.draw.rect(self.surface, 'green', rect)
