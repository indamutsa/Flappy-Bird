# Imports
import os
import pygame
import random
import time
import neat

# Local imports
from bird import Bird
from constants import WIN_WIDTH, WIN_HEIGHT, BIRD_IMGS, PIPE_IMGS, BASE_IMG, BG_IMG

# Let us draw the bird
def draw_window(win, bird):
    win.blit(BG_IMG, (0,0)) # Draw the background image
    bird.draw(win) # Draw the bird
    pygame.display.update() # Update the display
    
# Main function
def main():
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30) # 30 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        bird.move()
        draw_window(win, bird)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()