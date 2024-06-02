import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Загружаем изображение корабля и изменяем его размер
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Изменяем размер изображения
        self.rect = self.image.get_rect()
        
        # Начальное положение корабля - середина нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
