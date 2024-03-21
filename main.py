import pygame
from grid import newGrid

#setting
tick_speed = 2 # durée d'un tick en ms

cell_size = 2 # Taille d'une cellule en pixels
horizontal_cells = 400 # nombre de cellule sur le plan horizontal
vertical_cells = 400 # nombre de cellule sur le plan vertical
screen_size = (horizontal_cells * cell_size, vertical_cells * cell_size)

class newGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.grid = newGrid(self.screen, cell_size)
        self.time_since_last_tick = 0

        self.run()

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                self.grid.fruit_spawn_pattern = "line"
            elif keys[pygame.K_a]:
                self.grid.fruit_spawn_pattern = "even"
            elif keys[pygame.K_SPACE]:
                self.grid.spawnRandMicrobes(1)

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            self.time_since_last_tick += self.dt
            if self.time_since_last_tick > tick_speed:
                self.time_since_last_tick -= tick_speed
                self.grid.updateAll()

            # draw elts
            self.grid.draw()

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in ms since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60)

        pygame.quit()

jeu = newGame()