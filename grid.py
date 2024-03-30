import pygame
from food import *
from microbes import Microbe
import microbes
import debuger
import random
import pos
import debuger
from setting import *

class Grid:
    def __init__(self, surface: pygame.surface.Surface, screenWorld : pos.Pos, cell_size) -> None:
        self.screenWorld = screenWorld
        self.surface = surface
        self.cell_size = cell_size
        self.horizontal_cell_count = screenWorld.x // cell_size
        self.vertical_cell_count = screenWorld.y // cell_size

        self.food_matrix = foodMatrix(self.vertical_cell_count, self.horizontal_cell_count, surface, self.screenWorld, self.cell_size)

        self.microbeID = 0

        self.debug = debuger.Debuger()
        self.debug.activateDebugMode(False)

        self.food_list = []
        self.microbe_list = []

        self.spawnRandMicrobes(initial_microbes_count)
        
    def spawnRandMicrobes(self, count = 1):
        for i in range(count):
            self.addMicrobe()

    def addMicrobe(self, pos_x = 0, pos_y = 0, customGene = 0, direction = 0):
        self.microbeID += 1
        this_microbeID = self.microbeID

        if pos_x == 0:
            pos_x = random.randrange(self.horizontal_cell_count)
        if pos_y == 0:
            pos_y = random.randrange(self.vertical_cell_count)
        if customGene == 0:
            microbe = Microbe(self.screenWorld, pos.Pos(pos_x,pos_y), self.cell_size, id =this_microbeID)
        else : 
            microbe = Microbe(self.screenWorld, pos.Pos(pos_x,pos_y), self.cell_size, id = this_microbeID, customGene=customGene, hasParent=True, initialDirectionIndex=direction)

        self.microbe_list.append(microbe)
        return microbe

    def updateAll(self):
        self.food_matrix.fruitsSpawningRoutine()
        for elt in self.microbe_list:
            energy_used = elt.update()
            self.fruitsEating(elt)
            if elt.energy > microbes.energy_to_reproduce:
                elt.energy = elt.energy // 2
                child = self.addMicrobe(elt.pos.x, elt.pos.y, elt.gene, elt.direction)

        self.killDeadMicrobes()

    def killDeadMicrobes(self):
        # microbes_to_kill_indexes = []
        self.microbe_list = [elt for elt in self.microbe_list if elt.energy >0]
        # for i in range(len(self.microbe_list)):
        #     if self.microbe_list[i].energy < 0:
        #         microbes_to_kill_indexes.append(i)

        # microbes_to_kill_indexes.reverse()
        # for index in microbes_to_kill_indexes:
        #     del self.microbe_list[index]

    def fruitsEating(self, microbe):
        #if microbe.energy < microbe.maximum_energy:
        eaten_fruits = self.food_matrix.eatFood(int(microbe.pos.x), int(microbe.pos.y))
        while (eaten_fruits !=0) and ((microbe.energy + energy_per_food) < microbe.maximum_energy):
            microbe.eat(eaten_fruits)
            eaten_fruits = self.food_matrix.eatFood(int(microbe.pos.x), int(microbe.pos.y))
            
    def draw(self):
        self.food_matrix.draw()
        for microbe in self.microbe_list:
            color, top_left, size = microbe.draw()
            pygame.draw.rect(self.surface, color, pygame.rect.Rect(top_left, size))
