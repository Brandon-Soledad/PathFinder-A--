import pygame
import sys

def createGrid():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    WHITE = (255,255,255)

    pygame.init()
    frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PathFinder")
    frame.fill(WHITE)

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

def main():
    createGrid()
if __name__ == '__main__':
    main()    