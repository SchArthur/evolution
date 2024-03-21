import pygame
import random
import math

extrude = 1 # nombre de pixels qui dépassent de la case
step_index = [pygame.Vector2(-1,1),
              pygame.Vector2(0,1),
              pygame.Vector2(1,1),
              pygame.Vector2(-1,0),
              pygame.Vector2(1,0),
              pygame.Vector2(-1,-1),
              pygame.Vector2(0,-1),
              pygame.Vector2(1,-1)]

empty_gene = [random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000),
              random.randint(0,1000)]

move_cost = [0,1,2,4,8,4,2,1]

geneMaxMutationValue = 1000
energy_per_food = 40
initial_energy = 500
energy_to_reproduce = 1000
energy_lost_per_tick = 1

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

class newMicrobe:
    def __init__(self, surface : pygame.surface.Surface, pos : pygame.Vector2, cell_size, id, customGene : list = empty_gene, hasParent = False, energy = initial_energy , initialDirectionIndex = 0) -> None:
        self.surface = surface
        self.cell_size = cell_size
        self.pos = pos
        self.energy = energy

        self.age = 0
        self.id = id

        if hasParent :
            self.gene = self.mutateGene(customGene.copy())
        else:
            self.gene = customGene.copy()
            self.getRandomGene()

        #self.direction = random.randrange(len(step_index))
        self.direction = initialDirectionIndex
        # print(self.gene)

    def getGeneLength(self):
        sum = 0

        for i in range(len(self.gene)):
            sum += self.gene[i]

        return sum
    
    def getRandomGene(self):
        for i in range(len(self.gene)):
            self.gene = self.mutateGene(self.gene, i)
    
    def mutateGene(self, gene, i = -1):
        new_genes = gene

        if i == -1:
            i = random.randrange(len(new_genes))
        mutation = random.randrange(geneMaxMutationValue)
        mutation -= mutation//2
        new_genes[i] += mutation
        if new_genes[i] < 0:
            new_genes[i] = 0

        sum = 0
        for i in range(len(new_genes)):
            sum += new_genes[i]
        biggest = max(new_genes)

        for i in range(len(new_genes)):
            new_genes[i] = mapNumbers(biggest, 1000, new_genes[i])

        return new_genes
    
    def eat(self, quantity):
        self.energy += energy_per_food * quantity

    def update(self):
        energy_used = self.move()
        energy_used += energy_lost_per_tick
        self.energy -= energy_used
        self.age += 1

        return energy_used
            
    def getGeneDirection(self):
        somme = 0
        for i in range(len(self.gene)):
            somme += self.gene[i]

        rnd = random.randrange(somme)
        
        somme = 0
        for i in range(len(self.gene)):
            somme += self.gene[i]
            if somme > rnd:
                return i

    def move(self):
        energy_used = 0
        gene_dir = self.getGeneDirection()
        energy_used += move_cost[gene_dir]
        direction_index = correct_direction(gene_dir + self.direction)
        self.direction = direction_index
        self.pos += step_index[direction_index]
        if self.pos.x < 0:
            self.pos.x = (self.surface.get_width() // self.cell_size) - 1
        elif self.pos.x > (self.surface.get_width() // self.cell_size) - 1:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = (self.surface.get_height() // self.cell_size) - 1
        elif self.pos.y > (self.surface.get_height() // self.cell_size) - 1:
            self.pos.y = 0

        return energy_used

    def draw(self):
        top = (self.pos[0] * self.cell_size) - extrude
        left = (self.pos[1] * self.cell_size) - extrude
        top_left = (top, left)
        size = (self.cell_size + extrude * 2, self.cell_size + extrude * 2)
        rect = pygame.rect.Rect(top_left, size)
        pygame.draw.rect(self.surface, 'blue', rect)

    def getGeneSTR(self):
        geneSTR = ''
        for i in range(len(self.gene)):
            geneSTR += (str(self.gene[i]) + ',')
        geneSTR[:-1]
        return geneSTR