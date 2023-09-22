'''
We are creating a pipe class that will be used to create the pipes in the game.
A pipe is going to have an image, an x position, and a height.
We are going to have a top pipe and a bottom pipe. Essentially, the flappy bird is going to have to fly through the gap between the top pipe and the bottom pipe.
'''
import pygame
import random

# Local imports
from constants import WIN_WIDTH, WIN_HEIGHT, PIPE_IMG


class Pipe:
    GAP = 200 # Gap between the top and bottom pipe
    VEL = 5 # How fast the pipe is going to move
    
    def __init__(self, x): # x is the x position of the pipe, we are using x because the pipe is going to move from right to left
        self.x = x # x position of the pipe
        self.height = 0 # Height of the pipe
        self.gap = 100 # Gap between the top and bottom pipe
        
        self.top = 0 # Top pipe
        self.bottom = 0 # Bottom pipe
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True) # Flip the pipe image
        self.PIPE_BOTTOM = PIPE_IMG # Bottom pipe
        
        self.passed = False # If the bird passed the pipe
        self.set_height() # Set the height of the pipe
        
    # Method to set the height of the pipe    
    def set_height(self):
        self.height = random.randrange(50, 450) # Random height between 50 and 450
        self.top = self.height - self.PIPE_TOP.get_height() # Top pipe
        self.bottom = self.height + self.GAP # Bottom pipe
        
    # Method to move the pipe
    def move(self):
        self.x -= self.VEL # Move the pipe from right to left
        
    # Method to draw the pipe
    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top)) # Draw the top pipe
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom)) # Draw the bottom pipe
        
    def collide(self, bird):
        bird_mask = bird.get_mask() # Mask for the bird to detect collision
        top_mask = pygame.mask.from_surface(self.PIPE_TOP) # Mask for the top pipe
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM) # Mask for the bottom pipe
        
        # Offset is the distance between the bird and the pipe - How can we check the distance between the bird and the pipe?
        # We can check the distance between the bird and the pipe by subtracting the bird mask from the top mask and the bottom mask
        # If the bird is colliding with the top pipe, the offset is going to be a negative number
        # If the bird is colliding with the bottom pipe, the offset is going to be a positive number
        top_offset = (self.x - bird.x, self.top - round(bird.y)) # Offset for the top pipe
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        