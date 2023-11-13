# Developping Flappy Bird with Pygame : AI enabled

In this project, I will develop the famous game Flappy Bird with Pygame. The game will be AI enabled, which means that the computer will play the game instead of the player. The AI will be developed with the NEAT algorithm.

## Introduction

Flappy Bird is a game developed by Dong Nguyen in 2013. The goal of the game is to keep a bird alive as long as possible by avoiding obstacles. The bird flies continuously and the player only has to press the space bar to make the bird fly up. If the bird hits an obstacle or falls to the ground, the game is over.

NEAT (NeuroEvolution of Augmenting Topologies) is a genetic algorithm for the generation of evolving artificial neural networks. It is a method for evolving arbitrary neural networks. NEAT is based on applying three key techniques: tracking genes with history markers, applying speciation (the evolution of species) to preserve innovations, and developing topologies incrementally from simple initial structures ("complexifying"). It was developed by Kenneth O. Stanley while at The University of Texas at Austin. NEAT has been applied to a number of reinforcement learning tasks, including the evolution of a neural network to play checkers.

## Requirements

- Python 3.6 or higher
- Pygame
- NEAT
- Graphviz

## Installation

We will start by specifying or the requirements in a file called requirements.txt. This file will be used by pip to install all the required packages. To specify the version of a package, we can check them with the following command:

```sh

pip freeze

# or
pip show <package_name>
pip list
```

```sh
pygame==2.5.2
neat-python==0.92
graphviz==0.16
```

Then, we will install all the requirements with the following command:

```sh
pip install -r requirements.txt
```

We will then create a virtual environment to isolate the project from the rest of the system. This will allow us to install the required packages without affecting the rest of the system.

```sh
# Create the virtual environment
python -m venv pyenv

# Activate the virtual environment
source pyenv/bin/activate
```

---

First let us understand the game logic. We will use object oriented programming to create the game.
So we need to understand which objects we need to create.
We need to create the following objects:

- Bird
- Pipe
- Ground

So we start developing these claasses first.

## Understanding PEXEL PERFECT COLLISION in flappy bird

---

But first, let's understand what pixel perfect collision is.

Pixel-perfect collision detection is a type of collision detection mechanism that takes into account the actual shape of the object right down to the pixel level. This is in contrast to simpler bounding box or circle-based collision detection, which only use simple geometric shapes to approximate object boundaries.

In pixel-perfect collision detection, each object is represented by a 2D array (the mask) where each element corresponds to a pixel in the object's image. This array specifies which pixels are "solid" (part of the object) and which are "empty" (transparent or outside the object).

Here's a simplified example to demonstrate:

1. Imagine two objects: `A` and `B`. Each object's shape is represented in a 3x3 mask.

   - Object A (a diagonal line from top-left to bottom-right):

     ```
     1 0 0
     0 1 0
     0 0 1
     ```

   - Object B (a diagonal line from top-right to bottom-left):
     ```
     0 0 1
     0 1 0
     1 0 0
     ```

2. To check for collisions, you'd place these masks over each other, taking into account their relative positions (the offset).

3. For each overlapping "solid" pixel from both masks, you confirm a collision.

The benefit of pixel-perfect collision detection is its high accuracy, especially for irregular shapes. However, this comes at the cost of computational complexity. For simpler shapes, or when absolute accuracy is not necessary, other methods like bounding boxes or circles may be more efficient.

In Python, using Pygame as mentioned in the previous answer, you can achieve pixel-perfect collision using masks and the `overlap` method, which performs this operation efficiently under the hood.

---

Back to our game Flappy Bird, mask-based collision detection is often used to determine whether the bird collides with an obstacle like a pipe. The concept of a mask here refers to a 2D array of boolean values representing the actual shape of an object in a pixel-perfect way.

Let's assume you have the images of the bird and a pipe loaded as Pygame surfaces. You would generate masks for them as follows:

```python
import pygame

# Initialize Pygame
pygame.init()

# Load images
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.png")

# Generate masks
bird_mask = pygame.mask.from_surface(bird_image)
pipe_mask = pygame.mask.from_surface(pipe_image)
```

To check for collisions, you'll typically do the following:

1. Calculate the offset between the bird and pipe.
2. Use the mask's `overlap` function to check for a collision point.

Here's some Python code using Pygame that demonstrates this:

```python
# Position (x, y) of bird and pipe
bird_position = [50, 50]
pipe_position = [100, 30]

# Calculate offset
offset_x = pipe_position[0] - bird_position[0]
offset_y = pipe_position[1] - bird_position[1]

# Check for collision
collision_point = bird_mask.overlap(pipe_mask, (offset_x, offset_y))

# If collision_point is None, no collision occurred. Otherwise, a collision happened.
if collision_point:
    print(f"Collision occurred at {collision_point}")
else:
    print("No collision")
```

In this example, if `collision_point` is not `None`, then a collision occurred at the point returned by the `overlap` function. This allows for a very accurate collision detection.

This approach should provide a good balance of accuracy and performance, especially for irregularly shaped objects like the bird and pipes in Flappy Bird.

---

Course by _[Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg)_

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/OGHA-elMrxI/0.jpg)](https://github.com/indamutsa/Flappy-Bird/tree/main/images)

---

## Integrating NEAT (NeuroEvolution of Augmenting Topologies) into Flappy Bird

NEAT which stands for NeuroEvolution of Augmenting Topologies is a genetic algorithm for the generation of evolving artificial neural networks. It is a method for evolving arbitrary neural networks. NEAT is based on applying three key techniques: tracking genes with history markers, applying speciation (the evolution of species) to preserve innovations, and developing topologies incrementally from simple initial structures ("complexifying"). It was developed by Kenneth O. Stanley while at The University of Texas at Austin. NEAT has been applied to a number of reinforcement learning tasks, including the evolution of a neural network to play checkers.

Each neural networks has input layers, hidden layers and output layers. The input layers are the inputs of the neural network. The hidden layers are the layers between the input and output layers. The output layers are the outputs of the neural network. The neural network will take the inputs, process them through the hidden layers and output the outputs.

In our scenario, the inputs will be the bird's y position, the distance between the bird and the next pipe and the distance between the bird and the next pipe's bottom. _The outputs will be the jump or not jump decision_. We also have connections between the nodes. The connections are the weights of the neural network. The weights are the values that will be multiplied by the inputs to get the outputs. The weights will be adjusted by the NEAT algorithm. Once this is done, we will add the bias to the weights. The bias is a constant value that will be added to the weighted sum of the inputs. The bias will be adjusted by the NEAT algorithm.

At the end, we add an activation function to the output layer. The activation function will determine the output of the neural network. In our case, we will use the sigmoid function as the activation function. The sigmoid function will return a value between 0 and 1. If the value is greater than 0.5, the bird will jump. If the value is less than 0.5, the bird will not jump. We will use TanH as the activation function for the hidden layers. TanH will return a value between -1 and 1.

It is important to note that the weights, bias and activation functions will be adjusted by the NEAT algorithm. The NEAT algorithm will also add and remove nodes and connections. The NEAT algorithm will also add and remove hidden layers. So we don't have to manually add connections between the nodes.

### Approach

1. Let us start by creating a random population of birds. Each bird has a neural networks that controls its movement.
2. We test each of these networks and evaluate their fitness. The fitness is the score of the bird. The score is the number of pipes the bird has passed.
3. We select the best birds and use them to create the next generation of birds. We do this by applying crossover and mutation to the best birds. How does NEAT breed and mutate the next generation? Here is the [paper](https://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf) that explains the [NEAT algorithm](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).

---

The outputs will be either we jump or we don't jump. Hence we need one neuron. We will use TanH as the activation function for the hidden layers. TanH will return a value between -1 and 1. It is important to note that the weights, bias and activation functions will be adjusted by the NEAT algorithm. The NEAT algorithm will also add and remove nodes and connections. The NEAT algorithm will also add and remove hidden layers. So we don't have to manually add connections between the nodes.

---

Inputs: Bird y position, top pipe y position, bottom pipe y position
Outputs: Jump or not jump. One neuron
Activation function: TanH
Population size: 100
Fitness function: How good our birds are. The fitness is the score of the bird. The score is the number of pipes the bird has passed.
Max Generations: 30
