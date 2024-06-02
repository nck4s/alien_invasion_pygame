import pygame

class Character:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Загружаем изображение персонажа и получаем его прямоугольник
        self.image = pygame.image.load('images/cosmonaut.bmp')
        self.rect = self.image.get_rect()
        
        # Начальное положение персонажа - центр экрана
        self.rect.center = self.screen_rect.center

    def blitme(self):
        # Рисуем персонажа в текущей позиции
        self.screen.blit(self.image, self.rect)
