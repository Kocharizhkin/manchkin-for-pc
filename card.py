import pygame
class Card:
        def __init__(self, screen):
            self.speed = 2
            self.screen = screen
            self.image = pygame.image.load("cards/РасовыйКоктейль.png")
            self.image = pygame.transform.scale(self.image, (210, 300))
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
            self.moving_right = False
            self.moving_left = False

        def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx += self.speed
            if self.moving_left and self.rect.left > self.screen_rect.left:
                self.rect.centerx -= self.speed

        def blitme(self):
            self.screen.blit(self.image, self.rect)