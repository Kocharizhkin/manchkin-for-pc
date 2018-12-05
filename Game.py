import pygame
import sys

playScreen=pygame.image.load('data\GameForm\PlayScreen.png')
playScreen=pygame.transform.scale(playScreen, (1368,768))

class Game:
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen.blit(playScreen, (0, 0))
        while True:
            for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     sys.exit()
            pygame.display.flip()