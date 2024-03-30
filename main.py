import pygame
import pos
from grid import Grid
from setting import *
import debuger

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.dt = 0
        #indique la taille en pixel du monde dans lequel on évolue
        self.screenWorld = pos.Pos(self.screen.get_width(), self.screen.get_height())

        self.grid = Grid(self.screen, self.screenWorld, cell_size)
        self.time_since_last_tick = 0
        self.tick_speed = tick_speed
        self.tick_count = 0

        self.run()

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handler_keys()


            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            self.time_since_last_tick += self.dt
            while self.time_since_last_tick > self.tick_speed:
                self.time_since_last_tick -= self.tick_speed
                self.tick_count += 1
                self.grid.updateAll()

            # draw elts
            self.grid.draw()

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in ms since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60)

        debuger.mainDebugger.write_content()
        pygame.quit()

    def handler_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.grid.food_matrix.fruit_spawn_pattern = "line"
        elif keys[pygame.K_a]:
            self.grid.food_matrix.fruit_spawn_pattern = "even"
        elif keys[pygame.K_SPACE]:
            self.grid.spawnRandMicrobes(1)
        elif keys[pygame.K_KP_PLUS]:
            self.tick_speed +=5
        elif keys[pygame.K_KP_MINUS]:
            self.tick_speed -=5
            if self.tick_speed<tick_speed:
                self.tick_speed = tick_speed
    
jeu = Game()