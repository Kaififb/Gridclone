import pygame
import os

clock = pygame.time.Clock()

size = 14
width = 700
height = 700
columns = int(width / size)
rows = int(height / size)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (width/2 + 100,50)

Board = []

Foods = []
testcell = [['JE', '675', '603', 'Nm', '0.76', '0.2', 'KfsW', 'ROf'],
['MO', '934', '802', 'Qa', '0.65', '0.2', 'tqnn', 'TGB']]

screen = pygame.display.set_mode((width,height))