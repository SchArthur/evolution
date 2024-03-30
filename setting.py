import pygame

# ----- DEBUG MODE -----

DEBUG_MODE = True

# ----- KEYS -----
key_line = pygame.K_z
key_even = pygame.K_a
key_spawn_one = pygame.K_SPACE
key_pause = pygame.K_p
key_play = pygame.K_o

def getKeysSettingsSTR() -> str:
    text = ""
    text += getControlKeysSTR("NOURRITURE EN LIGNES", key_line)
    text += getControlKeysSTR("NOURRITURE EPARPILLEES", key_even)
    text += getControlKeysSTR("PAUSE", key_pause)
    text += getControlKeysSTR("PLAY", key_play)
    text += getControlKeysSTR("AJOUTER UN MICROBE", key_spawn_one)

    return text

def getControlKeysSTR(action :str, key :int) -> str:
    text = ""
    text = "Pour " + action + " appuyez sur : " + pygame.key.name(key).upper() + " .\n"
    return text

# ----- FOOD -----
fruit_spawn_per_tick = 7

initial_fruits_count = 20000

v_line_fruits_step = 75
vertical_line_count = 4
h_line_fruits_step = 90
horizontal_line_count = 3
line_percent = 95


# ----- MICROBES -----
extrude = 1 # nombre de pixels qui dépassent de la case

maximum_energy = 1500
energy_per_food = 40
initial_energy = 500
energy_to_reproduce = 1000
energy_lost_per_tick = 1

# ----- GENES -----
SUM_GEN_MAX = 8000
NBR_GEN = 8
GEN_MAX = SUM_GEN_MAX // NBR_GEN
GEN_MUTATION_MAX = 500
move_cost_array = [0,1,2,4,8,4,2,1]

# ----- GRID -----
grid_color = 'gray'
initial_microbes_count = 50

# ----- MAIN -----
tick_speed = 3 # durée d'un tick en ms
cell_size = 2 # Taille d'une cellule en pixels
horizontal_cells = 400 # nombre de cellule sur le plan horizontal
vertical_cells = 400 # nombre de cellule sur le plan vertical
screen_size = (horizontal_cells * cell_size, vertical_cells * cell_size)