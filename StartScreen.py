import sys
import pygame
from Game import Game
game=Game()


StartScreen=pygame.image.load('data\GameForm\StartScreen.jpg')
StartScreen=pygame.transform.scale(StartScreen, (1368,768))


def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)


def run_game():
    pygame.init()
    screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.set_caption("Munchkin")
    screen.blit(StartScreen,(0,0))

    while True:
        exit_type = Buttonify('data\GameForm\ExitButton.png',(750,600),screen)
        start=Buttonify('data\GameForm\PlayButton.png',(900,300),screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if exit_type[1].collidepoint(mouse):
                    sys.exit()
                if start[1].collidepoint(mouse):
                    game.start()
                    sys.exit()

        pygame.display.flip()


run_game()