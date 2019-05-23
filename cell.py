import pygame
import random
import math

from config import screen, size, width, height, columns, rows
from neural_net import NeuralNet

class Cell():
    def __init__(self, listpos, direction, genome):
        self.listpos = listpos
        self.direction = direction # 0 = NORTH 1 = SOUTH 2 = EAST 3 = WEST
        self.genome = genome
        self.color = genome[0]
        self.neurons = self.genome
        del self.neurons[0]
        self.net = NeuralNet(self.neurons)
        self.energy = 40000

    def display(self):
        self.x = (self.listpos % columns) * size
        self.y = math.floor(self.listpos / rows) * size
        pygame.draw.rect(screen,self.color,(self.x,self.y,size,size))
    
    def run(self):
        self.net.neuron_check(self.listpos)
            
