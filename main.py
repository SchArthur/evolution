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

        print(getKeysSettingsSTR())

        self.grid = Grid(self.screen, self.screenWorld, cell_size)
        self.time_since_last_tick = 0
        self.tick_speed = tick_speed
        self.tick_count = 0

        self.speed_factor = 1

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

            self.time_since_last_tick += self.dt * self.speed_factor 
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
        if keys[key_line]:
            self.grid.food_matrix.fruit_spawn_pattern = "line"
        elif keys[key_even]:
            self.grid.food_matrix.fruit_spawn_pattern = "even"
        elif keys[key_spawn_one]:
            self.grid.spawnRandMicrobes(1)
        elif keys[key_pause]:
            if self.speed_factor != 0:
                self.speed_factor = 0
                print("Game paused")
                print("Appuyez sur " + (pygame.key.name(key_play)).capitalize() + " pour reprendre")
        elif keys[key_play]:
            if self.speed_factor != 1:
                self.speed_factor = 1
                print("Game resumed")
                print("Appuyez sur " + (pygame.key.name(key_pause)).capitalize() + " pour mettre en pause")
        elif keys[pygame.K_KP_PLUS]:
            self.tick_speed +=5
        elif keys[pygame.K_KP_MINUS]:
            self.tick_speed -=5
            if self.tick_speed<tick_speed:
                self.tick_speed = tick_speed
    
jeu = Game()