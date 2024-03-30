import random
import math
import pos
import genes
import debuger

from setting import *
from utils import *

step_index = [pos.Pos(-1,1),
              pos.Pos(0,1),
              pos.Pos(1,1),
              pos.Pos(-1,0),
              pos.Pos(1,0),
              pos.Pos(-1,-1),
              pos.Pos(0,-1),
              pos.Pos(1,-1)]


def correct_direction(Index) -> int:
    dirIndex = Index
    if dirIndex >= len(step_index):
        dirIndex -= len(step_index)
    elif dirIndex < 0 :
        dirIndex += len(step_index)

    return dirIndex

def mapNumbers(input_end, output_end, value, input_start = 0, output_start = 0) -> int:
    slope = (output_end - output_start) / (input_end - input_start)
    output = output_start + slope * (value - input_start)
    output = math.ceil(output)
    return output

class Microbe:
    def __init__(self, surfacePos: pos.Pos, pos : pos.Pos, cell_size, id, customGene : list = None, hasParent = False, energy = initial_energy , initialDirectionIndex = 0) -> None:
        self.surfacePos = surfacePos
        self.cell_size = cell_size
        self.pos = pos
        self.energy = energy
        self.maximum_energy = maximum_energy

        self.hasParent = hasParent

        self.age = 0
        self.id = id

        if hasParent :
            self.parentGene = customGene.gene.copy()
            self.gene = genes.GeneMovement(customGene)
        else:
            self.gene = genes.GeneMovement()

        self.direction = self.gene.getGeneDirection()

        debuger.mainDebugger.microbesSpawnDebug(self)
    
    def eat(self, quantity):
        self.energy += energy_per_food * quantity
        if self.energy > maximum_energy :
            self.energy = maximum_energy

    def getInfos(self) -> str :
        text = ""
        text += "MICROBE ID : " + str(self.id) + "\n"
        text += "AGE : " + str(self.age) + " frames\n"
        text += "Gene : " + str(self.gene.getGene()) + "\n"
        text += "A un parent : " + str(self.hasParent) + "\n"
        if self.hasParent : 
            text += "Gene parent : " + str(self.parentGene) + "\n"

        return text

    def update(self):
        energy_used = self.move()
        self.energy -= energy_used
        self.age += 1

        return energy_used
            
    def move(self):
        energy_used = energy_lost_per_tick
        gene_dir = self.gene.getGeneDirection()
        energy_used += move_cost_array[gene_dir]
        direction_index = (gene_dir + self.direction)%8
        self.direction = direction_index
        self.pos += step_index[self.direction]
        if self.pos.x < 0:
            self.pos.x = (self.surfacePos.x // self.cell_size) - 1
        elif self.pos.x > (self.surfacePos.y // self.cell_size) - 1:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = (self.surfacePos.x // self.cell_size) - 1
        elif self.pos.y > (self.surfacePos.y // self.cell_size) - 1:
            self.pos.y = 0

        return energy_used

    def draw(self):
        top = (self.pos.x * self.cell_size) - extrude
        left = (self.pos.y * self.cell_size) - extrude
        top_left = (top, left)
        size = (self.cell_size + extrude * 2, self.cell_size + extrude * 2)
        #rect = pygame.rect.Rect(top_left, size)
        return self.getColor(), top_left, size
        #pygame.draw.rect(surface, 'blue', rect)

    def getColor(self):
        """Renvoie sa couleur, reflétant son énergie"""
        v = 255-max(min(int(self.energy*255/initial_energy),255),0)
        return v,v,255