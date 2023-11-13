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

pygame.font.init()  # Initialize the font
STAT_FONT = pygame.font.SysFont("comicsans", 50)  # Font to display the score

# Let us draw the bird


def draw_window(win, birds, pipes, base, score):
    win.blit(BG_IMG, (0, 0))  # Draw the background image

    # Drawing the pipes
    for pipe in pipes:
        pipe.draw(win)

    # Draw the score
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))  # Draw the score

    base.draw(win)  # Draw the base

    for bird in birds:
        bird.draw(win)  # Draw the bird

    pygame.display.update()  # Update the display

# Main function


def main(genomes, config):
    nets = []  # Neural networks
    ge = []  # Genomes
    birds = []  # List of birds

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(
            g, config)  # Create a neural network
        nets.append(net)  # Add the neural network to the list
        birds.append(Bird(230, 350))  # Add a bird to the list
        g.fitness = 0  # Set the fitness to 0
        ge.append(g)  # Add the genome to the list

    base = Base(730)  # Create a base object
    pipes = [Pipe(600)]  # Create a pipe object

    # Create a window to display the game
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()  # Create a clock to control the frames per second

    run = True  # Run the game
    score = 0  # Score of the game when the bird passes the pipe

    while run:
        clock.tick(30)  # 30 frames per second
        for event in pygame.event.get():  # Get the events
            if event.type == pygame.QUIT:  # If the user clicks the close button
                run = False  # Stop the game

                pygame.quit()
                quit()

        pipe_ind = 0  # Index of the pipe

        # If there is more than one pipe, check which pipe to use
        if (len(birds) > 0):
            # If the bird has passed the first pipe
            if (len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width()):
                pipe_ind = 1
        else:
            run = False
            break

        for x, bird in enumerate(birds):  # Loop through the birds
            bird.move()  # Move the bird
            # Increase the fitness of the bird to encourage it to move forward
            ge[x].fitness += 0.1

            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(
                bird.y - pipes[pipe_ind].bottom)))  # Get the output from the neural network

            if output[0] > 0.5:  # If the output is greater than 0.5, jump to avoid the pipe
                bird.jump()

        # Move the pipes
        '''
        We need to create a pipe object every time the pipe is off the screen.
        We will handle this in the for loop below.
        '''

        rem = []  # List of pipes to remove
        add_pipe = False  # Add a pipe

        for pipe in pipes:
            for x, bird in enumerate(birds):
                # If the bird is colliding with the pipe, stop the game
                if pipe.collide(bird):
                    ge[x].fitness -= 1  # Decrease the fitness
                    birds.pop(x)  # Remove the bird
                    nets.pop(x)  # Remove the neural network
                    ge.pop(x)  # Remove the genome

                # If we have passed the pipe, add another pipe to the screen to keep the game going
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            # If the pipe is off the screen, remove the pipe
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()  # Move the pipe

        # If the bird passes the pipe, increase the score and add another pipe
        if add_pipe:
            score += 1  # Increase the score
            for g in ge:
                g.fitness += 5  # Increase the fitness to encourage the bird to pass the pipe

            pipes.append(Pipe(600))  # Add a pipe

        # Next, we need to remove the pipes that are off the screen
        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            # If the bird hits the ground, stop the game
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)  # Remove the bird
                nets.pop(x)  # Remove the neural network
                ge.pop(x)  # Remove the genome

        # Draw the window to display the game
        draw_window(win, birds, pipes, base, score)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)  # Load the configuration file

    # Create a population
    p = neat.Population(config)

    # Add a reporter to show the progress in the terminal
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()

    p.add_reporter(stats)  # Add a reporter to show the statistics

    # Run the main function (which is was configured to be the fitness function) 50 times
    winner = p.run(main, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "feedforward-config.txt")
    run(config_path)
