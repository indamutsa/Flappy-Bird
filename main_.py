# Imports
import os
import pygame
import random
import time
import neat

# Local imports
from bird import Bird
from pipe import Pipe
from base import Base
from constants import WIN_WIDTH, WIN_HEIGHT, BIRD_IMGS, PIPE_IMG, BASE_IMG, BG_IMG

pygame.font.init() # Initialize the font
STAT_FONT = pygame.font.SysFont("comicsans", 50) # Font to display the score

# Draw the game window
def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(win)
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()

# Main function
def main():
    bird = Bird(230, 350) # Create a bird object
    base = Base(730) # Create a base object
    pipes = [Pipe(600)] # Create a pipe object
    
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE) # Create a window to display the game
    clock = pygame.time.Clock() # Create a clock to control the frames per second
    
    run = True # Run the game
    score = 0 # Score of the game when the bird passes the pipe

    # New variables for bird speed (added)
    bird_velocity_x = 0  
    bird_velocity_y = 0  
    acceleration_y = 1  
    acceleration_x = 0  
    max_velocity_x = 5  
    
    while run:
        clock.tick(30) # 30 frames per second
        for event in pygame.event.get(): # Get the events
            if event.type == pygame.QUIT: # If the user clicks the close button
                run = False # Stop the game
            elif event.type == pygame.VIDEORESIZE: # If the user resizes the window
                # Resize the window and redraw the contents
                win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                draw_window(win, bird, pipes, base, score)    
                
            # Handling speed change (added)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_velocity_y -= acceleration_y
                elif event.key == pygame.K_DOWN:
                    bird_velocity_y += acceleration_y
                elif event.key == pygame.K_LEFT:
                    acceleration_x = -0.1
                elif event.key == pygame.K_RIGHT:
                    acceleration_x = 0.1
                    
            # Handling speed change stop (added)
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    bird_velocity_y = 0
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    acceleration_x = 0

        # Update bird position (added)
        bird_velocity_x = min(max_velocity_x, bird_velocity_x + acceleration_x)
        bird_velocity_x = max(-max_velocity_x, bird_velocity_x)
        bird.y += bird_velocity_y
        bird.x += bird_velocity_x
        
        base.move() # Move the base
        
        # Move the pipes
        '''
        We need to create a pipe object every time the pipe is off the screen.
        We will handle this in the for loop below.
        '''
        
        rem = [] # List of pipes to remove
        add_pipe = False # Add a pipe
        
        for pipe in pipes:            
            # If the bird is colliding with the pipe, stop the game
            if pipe.collide(bird):
                pass
            
            # If the pipe is off the screen, remove the pipe
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
                
            # If we have passed the pipe, add another pipe to the screen to keep the game going
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True              
        
            pipe.move() # Move the pipe
        
        # If the bird passes the pipe, increase the score and add another pipe
        if add_pipe:
            score += 1 # Increase the score
            pipes.append(Pipe(600)) # Add a pipe
            
        # Next, we need to remove the pipes that are off the screen
        for r in rem:
            pipes.remove(r)    
            
        # If the bird hits the ground, stop the game
        if bird.y + bird.img.get_height() >= 730:
            pass
            
            
        draw_window(win, bird, pipes, base, score) # Draw the window to display the game
        
        
    pygame.quit()
    quit()

