import sys
import pygame
from card import Card
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((900,700))
    card=Card(screen)
    bg_color=(120,120,90)
    pygame.display.set_caption("Munchkin")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(x, y)
        screen.fill(bg_color)
        card.blitme()
        pygame.display.flip()
run_game()