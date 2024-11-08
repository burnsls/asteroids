import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
            
        for sprite in updatable:
            sprite.update(dt)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000  # limits FPS to 60
    
    return

if __name__ == "__main__":
    main()
    