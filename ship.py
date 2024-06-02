import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Загружаем изображение корабля и изменяем его размер
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Изменяем размер изображения
        self.rect = self.image.get_rect()
        
        # Начальное положение корабля - середина нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        
        # Флаги движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Обновляем позицию корабля на основе флагов движения
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def blitme(self):
        # Рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
