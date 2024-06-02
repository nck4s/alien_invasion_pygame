import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Загружаем изображение корабля и получаем его прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Начальное положение корабля - центр нижней части экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
