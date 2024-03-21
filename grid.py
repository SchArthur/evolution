import pygame
from food import newFood
from microbes import newMicrobe
import microbes
import random

grid_color = 'gray'
line_fruits_step = 50
initial_microbes_count = 50
fruit_spawn_per_tick = 2

max_fruits = 40000
initial_fruits_count = max_fruits//2

class newGrid:
    def __init__(self, surface : pygame.surface.Surface, cell_size) -> None:
        self.surface = surface
        self.cell_size = cell_size
        self.horizontal_cell_count = surface.get_width() // cell_size
        self.vertical_cell_count = surface.get_height() // cell_size

        self.food_list = []
        self.microbe_list = []

        self.spawnRandMicrobes(initial_microbes_count)
        
        self.spawnFruitsEven(initial_fruits_count)
        
        self.fruit_spawn_pattern = "line"

    def fruitsSpawning(self):
        if self.fruit_spawn_pattern == "line":
            self.spawnFruitsInLine(fruit_spawn_per_tick)
        elif self.fruit_spawn_pattern == 'even':
            self.spawnFruitsEven(fruit_spawn_per_tick)

    def spawnRandMicrobes(self, count = 1):
        for i in range(count):
            self.addMicrobe()

    def addMicrobe(self, pos_x = 0, pos_y = 0, customGene = 0, direction = 0):
        if pos_x == 0:
            pos_x = random.randrange(self.horizontal_cell_count)
        if pos_y == 0:
            pos_y = random.randrange(self.vertical_cell_count)
        if customGene == 0:
            microbe = newMicrobe(self.surface, pygame.Vector2(pos_x,pos_y), self.cell_size)
        else : 
            microbe = newMicrobe(self.surface, pygame.Vector2(pos_x,pos_y), self.cell_size, customGene, hasParent=True, initialDirectionIndex=direction)

        self.microbe_list.append(microbe)

    def addFood(self, pos_x = 0, pos_y = 0):
        """Fait apparaitre un fruit à une position aléatoire.
        
        Sauf si pos_x et/ou pos_y != 0"""
        if len(self.food_list) < max_fruits:
            if pos_x == 0:
                pos_x = random.randrange(self.horizontal_cell_count)
            if pos_y == 0:
                pos_y = random.randrange(self.vertical_cell_count)
            food = newFood(self.surface, pygame.Vector2(pos_x, pos_y),self.cell_size)
            self.food_list.append(food)

    def spawnFruitsEven(self, quantity = 200):
        for i in range(quantity):
            self.addFood()
    
    def spawnFruitsInLine(self, quantity = 200):
        for i in range(quantity):
            isVertical = random.randrange(2)
            if isVertical == 0:
                pos_x = random.randrange(line_fruits_step, self.horizontal_cell_count, line_fruits_step)
                pos_y = random.randrange(self.vertical_cell_count)
            else:
                pos_x = random.randrange(self.horizontal_cell_count)
                pos_y = random.randrange(line_fruits_step, self.vertical_cell_count, line_fruits_step)
            self.addFood(pos_x, pos_y)

    def updateAll(self):
        self.fruitsSpawning()
        for elt in self.microbe_list:
            elt.update()
            if elt.energy > microbes.energy_to_reproduce:
                elt.energy = elt.energy // 2
                self.addMicrobe(elt.pos.x, elt.pos.y, elt.gene, elt.direction)
        self.fruitsEating()
        self.killDeadMicrobes()

    def killDeadMicrobes(self):
        microbes_to_kill_indexes = []
        for i in range(len(self.microbe_list)):
            if self.microbe_list[i].energy < 0:
                microbes_to_kill_indexes.append(i)

        microbes_to_kill_indexes.reverse()
        for index in microbes_to_kill_indexes:
            del self.microbe_list[index]

    def fruitsEating(self):
        eaten_fruits = []
        for i in range(len(self.food_list)):
            for elt in self.microbe_list:
                if self.food_list[i].pos == elt.pos:
                    eaten_fruits.append(i)
                    elt.eat()

        eaten_fruits.reverse()
        for index in eaten_fruits:
            del self.food_list[index]
            
    def draw(self):
        """
        for x in range(self.horizontal_cell_count):
            origin = pygame.Vector2(x * self.cell_size, 0)
            end = pygame.Vector2(x * self.cell_size, self.surface.get_height())
            pygame.draw.line(self.surface, grid_color, origin, end)

        for y in range(self.vertical_cell_count):
            origin = pygame.Vector2(0, y * self.cell_size)
            end = pygame.Vector2(self.surface.get_width(), y * self.cell_size)
            pygame.draw.line(self.surface, grid_color, origin, end)
        """

        for fruit in self.food_list:
            fruit.draw()
        for microbe in self.microbe_list:
            microbe.draw()
