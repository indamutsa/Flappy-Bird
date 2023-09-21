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
