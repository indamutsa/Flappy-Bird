# Imports
import os
import pygame
import random
import time
import neat
from constants import BIRD_IMGS


# Let us create the classes:
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # How much the bird is going to tilt
    ROT_VEL = 20 # How much we are going to rotate on each frame
    ANIMATION_TIME = 5 # How long we are going to show each bird animation
    
    # Constructor, the starting position of the bird
    def __init__(self, x, y):
        self.x = x # Starting position at x axis
        self.y = y # Starting position at y axis
        self.tilt = 0 # How much the image is tilted
        self.tick_count = 0 # Physics of the bird, how many times we moved up or down
        self.vel = 0 # Velocity of the bird
        self.height = self.y # Height of the bird
        self.img_count = 0 # Which image we are showing
        self.img = self.IMGS[0] # Which image we are showing
        
        
    # Method to jump
    def jump(self):
        self.vel = -10.5 # Negative velocity to move up
        self.tick_count = 0 # Reset the tick count
        self.height = self.y # Where the bird jumped from
        
    # Method to move
    def move(self):
        self.tick_count += 1 # How many times we moved since the last jump
               
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2 # Displacement, how many pixels we are moving up or down
        
        # Terminal velocity: If we are moving down more than 16 pixels, we are going to cap it at 16 pixels
        if d >= 16:
            d = 16
            
        # If we are moving up, we are going to move up a little bit more
        if d < 0:
            d -= 2
            
        self.y = self.y + d # Update the y position
        
        # If we are moving up, we are going to tilt the bird up
        if d < 0 or self.y < self.height + 50:
            # If we are moving up, we are going to tilt the bird up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            # If we are moving down, we are going to tilt the bird down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
                
    # Method to draw the bird -- This is the method responsible the bird to flap its wings animation
    def draw(self, win):
        self.img_count += 1  # How many times we showed the current image

        # Show the first image if we are showing the first image
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]  # Show the first image
        elif self.img_count < self.ANIMATION_TIME * 2:  # If we are showing the second image
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:  # If we are showing the third image
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:  # If we are showing the second image
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:  # If we are showing the fifth image
            self.img = self.IMGS[0]  # Show the first image
            self.img_count = 0  # Reset the image count
            
        # If we are moving down, we are going to show the bird without flapping its wings
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
            
        # Rotate the image around the center
        rotated_image = pygame.transform.rotate(self.img, self.tilt) # Rotate the image
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center) # Rotate the image around the center
        win.blit(rotated_image, new_rect.topleft) # Draw the rotated image
        
    # Method to get the mask
    def get_mask(self):
        return pygame.mask.from_surface(self.img) # Get the mask of the image. It can be used to calculate pixel perfect collisions