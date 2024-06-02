import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.character = Character(self)  # Создаем экземпляр персонажа

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1 

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blitme()  # Отображаем персонажа

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
