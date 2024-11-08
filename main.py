import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player1.draw(screen)
        player1.update(dt)
        
        
        pygame.display.flip()
        
        dt = clock.tick(60)  # limits FPS to 60
    
    return

if __name__ == "__main__":
    main()
    