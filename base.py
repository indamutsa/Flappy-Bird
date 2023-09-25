'''
The base class is a flappy bird game is going to be the ground that the bird is going to be flying over.
The base is going to move from right to left. The logic is going to move two images of the base from right to left to give an illusion that the base is moving.
'''

# Local imports
from constants import BASE_IMG

class Base:
    VEL = 5 # Velocity of the base
    WIDTH = BASE_IMG.get_width() # Width of the base
    IMG = BASE_IMG # Image of the base
    
    def __init__(self, y): # y is the y position of the base
        self.y = y # y position of the base
        self.x1 = 0 # x position of the base
        self.x2 = self.WIDTH # x position of the base
        
    # Method to move the base
    def move(self):
        self.x1 -= self.VEL # Move the base from right to left
        self.x2 -= self.VEL # Move the base from right to left
        
        # If the base is off the screen, reset the base
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH # Reset the base
            
        if self.x2 + self.WIDTH < 0: 
            self.x2 = self.x1 + self.WIDTH # Reset the base
            
            
    # Method to draw the base
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y)) # Draw the base
        win.blit(self.IMG, (self.x2, self.y)) # Draw the base again, so that the base is going to be moving from right to left
        
        