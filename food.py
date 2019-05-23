import pygame
import random
import math

from neural_net import NeuralNet
from config import screen, size, width, height, columns, rows

class Food():
    def __init__(self, listpos, color):
        self.listpos = listpos
        self.color = color

    def display(self):
        self.x = (self.listpos % columns) * size
        self.y = math.floor(self.listpos / rows) * size
        pygame.draw.rect(screen,self.color,(self.x,self.y,size,size))