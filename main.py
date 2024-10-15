import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 400

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = SCREEN_HEIGTH - 70

#create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("T-REX GAME")