import pygame
import numpy
import random
import string
import math

from cell import Cell
from food import Food
from config import Board, Foods, screen, size, width, height, rows, columns, testcell

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
all_neurons = ('JE', 'MO', 'EY')

pygame.init()

pygame.display.set_caption("Gridclone")

FOODSPAWN = pygame.USEREVENT
pygame.time.set_timer(FOODSPAWN, 300)

for i in range(rows*columns):
    Board.append(None)
    Foods.append(None)

def main():
    running = True
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                listpos = round((math.floor((mouseY / size)) * rows + math.floor(mouseX / size)))
                if not Board[listpos]:
                    create_cell(listpos, None)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    create_cell(int(len(Board) / 2 + columns / 2), testcell)
                elif event.key == pygame.K_c:
                    Board.clear()
                    for i in range(rows*columns):
                        Board.append(None)
            if event.type == FOODSPAWN:
                while None in Foods:
                    listpos = round((math.floor((random.randint(0, height - 1) / size)) * \
                    (width / size) + math.floor(random.randint(0, width - 1) / size)))
                    if not Foods[listpos]:
                        break
                if None in Foods:
                    Foods[listpos] = Food(listpos, (0, 255, 0))
        screen.fill((0, 0, 0))
        board_run()
        pygame.display.flip()

def create_cell(listpos, genome):
    newcolor = list(numpy.random.choice(range(30, 256), size=3))
    if not genome:
        genome = []
        for i in range(0, 4):
            new_neuron = []
            new_neuron.append(random.choice(all_neurons)) #neuron type
            new_neuron.append(''.join(random.choice(string.digits) for i in range(3))) #neuron xyz
            new_neuron.append(''.join(random.choice(string.digits) for i in range(3))) #neuron range
            new_neuron.append(''.join(random.choice(alphabet) for i in range(2))) #neuron tag
            new_neuron.append(str(random.randint(1, 100) / 100))#neuron bias
            new_neuron.append(str(random.randint(1, 250) / 100)) #neuron threshold
            new_neuron.append(''.join(random.choice(alphabet) for i in range(4))) #neuron properties
            for j in range(0, random.randint(1, 4)): #neuron outputs
                new_neuron.append(''.join(random.choice(alphabet) for i in range(3)))
            genome.append(new_neuron)
    genome.insert(0, newcolor)
    Board[listpos] = Cell(listpos, random.randint(0, 3), genome) #listpos, direction, genome

def board_run():
    for i in Foods:
        if isinstance(i, Food):
            i.display()
    for i in Board:
        if isinstance(i, Cell):
            i.run()
            i.display()

if __name__=="__main__":
    main()

