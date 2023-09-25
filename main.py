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

# Let us draw the bird
def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0)) # Draw the background image
    
    # Drawing the pipes 
    for pipe in pipes:
        pipe.draw(win)
        
    # Draw the score
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10)) # Draw the score
    
    base.draw(win) # Draw the base   
    bird.draw(win) # Draw the bird 
    pygame.display.update() # Update the display
    
# Main function
def main():
    bird = Bird(230, 350) # Create a bird object
    base = Base(730) # Create a base object
    pipes = [Pipe(600)] # Create a pipe object
    
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE) # Create a window to display the game
    clock = pygame.time.Clock() # Create a clock to control the frames per second
    
    run = True # Run the game
    score = 0 # Score of the game when the bird passes the pipe
    
    while run:
        clock.tick(30) # 30 frames per second
        for event in pygame.event.get(): # Get the events
            if event.type == pygame.QUIT: # If the user clicks the close button
                run = False # Stop the game
            elif event.type == pygame.VIDEORESIZE: # If the user resizes the window
                # Resize the window and redraw the contents
                win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                draw_window(win, bird, pipes, base, score)    
                
        # bird.move() # Move the bird
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

if __name__ == "__main__":
    main()