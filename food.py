import pygame
import random
from setting import *

class foodMatrix:
    def __init__(self, matrix_height, matrix_width, surface, screenWorld,  cell_size) -> None:
        self.surface = surface
        self.screenWorld = screenWorld
        self.cell_size = cell_size
        self.matrix_size = (matrix_width, matrix_height)
        self.fruits_quantity = initial_fruits_count
        
        self.matrix = []

        for y in range(matrix_height):
            line = []
            self.matrix.append(line)
            for x in range(matrix_width):
                cell = []
                self.matrix[y].append(cell)
                self.matrix[y][x] = []

        self.fruit_spawn_pattern = "even"
        self.fruitsSpawningRoutine(initial_fruits_count)

    def spawnFruitsEven(self, quantity = 200):
        for i in range(quantity):
            x = random.randint(0, int(self.matrix_size[0] -1))
            y = random.randint(0, int(self.matrix_size[1] -1))
            self.addFood(x, y)
    
    def spawnFruitsInLine(self, quantity = 200):
        for i in range(quantity):
            rnd = random.randrange(100)
            if line_percent > rnd :
                line_spawn = True
            else:
                line_spawn = False

            if line_spawn :
                isVertical = random.randrange(2)
                if isVertical == 0:
                    pos_x = random.randrange(v_line_fruits_step, (v_line_fruits_step * vertical_line_count) + 1, v_line_fruits_step)
                    pos_y = random.randrange(self.matrix_size[1])
                else:
                    pos_x = random.randrange(self.matrix_size[0])
                    pos_y = random.randrange(h_line_fruits_step, (h_line_fruits_step * horizontal_line_count) + 1, h_line_fruits_step)
                self.addFood(pos_x, pos_y)
            else :
                self.spawnFruitsEven(1)

    def draw(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] != []:
                    for food in self.matrix[y][x]:
                        food.draw(self.surface)

    def fruitsSpawningRoutine(self, quantity = fruit_spawn_per_tick):
        if self.fruit_spawn_pattern == "line":
            self.spawnFruitsInLine(quantity)
        elif self.fruit_spawn_pattern == 'even':
            self.spawnFruitsEven(quantity)

    def spawnFoods(self, quantity):
        pass

    def addFood(self, x, y):
        pos = pygame.Vector2(x,y)
        self.matrix[y][x].append(newFood(pos, self.cell_size))
        self.fruits_quantity += 1
        return 1

    def eatFood(self, x, y) -> int:
        if self.matrix[y][x] != []:
            # food_at = len(self.matrix[y][x])
            # self.matrix[y][x] = []
            # self.fruits_quantity -= 1
            # return food_at
            self.matrix[y][x] = self.matrix[y][x][1:]
            self.fruits_quantity -= 1
            return 1
        else:
            return 0

    def printMatrix(self):
        print(self.matrix)

class newFood:
    def __init__(self, pos : pygame.Vector2, cell_size) -> None:
        self.cell_size = cell_size
        self.pos = pos

    def draw(self, surface):
        top_left = self.pos * self.cell_size
        size = (self.cell_size, self.cell_size)
        rect = pygame.rect.Rect(top_left, size)
        pygame.draw.rect(surface, 'green', rect)
