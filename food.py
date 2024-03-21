import pygame

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

    def addFood(self, x, y):
        pos = pygame.Vector2(x,y)
        self.matrix[y][x].append(newFood(self.surface, pos, self.cell_size))

    def removeFood(self, x, y) -> int:
        foodQuantity = len(self.matrix[y][x])
        self.matrix[y][x] = []
        return foodQuantity

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
