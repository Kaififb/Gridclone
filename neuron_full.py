import pygame
import time
import math

from config import Board, Foods, size, width, height, columns, rows

range_1_up = ('10','20','30','40','50','60','70','21','31','41','51','61','32','42','52','43')
range_1_down = ('45','36','46','56','27','37','47','57','67','18','28','38','48','58','68','78')
range_1_right = ('81','82','83','84','85','86','87','72','73','74','75','76','63','64','65','54')
range_1_left = ('02','03','04','05','06','07','12','13','14','15','16','23','24','25','43')

class NeuronDo(object):
    def __init__(self, neuron, listpos):
        self.listpos = listpos
        self.neuron = neuron
        self.string_convert(neuron[0]) #function, not variable

    def string_convert(self, argument):
        method = getattr(self, argument)
        return method()

    def determine_direction(self):
        relative_direction = None
        coords = self.neuron[1]
        if(coords[0] != coords[1] and int(coords[0]) + int(coords[1]) != 8):
            if (coords[:2]) in range_1_up:
                relative_direction = 0
            elif (coords[:2]) in range_1_down:
                relative_direction = 1
            elif (coords[:2]) in range_1_right:
                relative_direction = 2
            elif (coords[:2]) in range_1_left:
                relative_direction = 3
        else:
            return(4)
        if Board[self.listpos].direction == 0:
            if relative_direction == 0:
                return(1)
            elif relative_direction == 1:
                return(0)
            elif relative_direction == 2:
                return(3)
            elif relative_direction == 3:
                return(2)
        elif Board[self.listpos].direction == 1:
            if relative_direction == 0:
                return(0)
            elif relative_direction == 1:
                return(1)
            elif relative_direction == 2:
                return(2)
            elif relative_direction == 3:
                return(3)
        elif Board[self.listpos].direction == 2:
            if relative_direction == 0:
                return(3)
            elif relative_direction == 1:
                return(2)
            elif relative_direction == 2:
                return(0)
            elif relative_direction == 3:
                return(1)
        elif Board[self.listpos].direction == 3:
            if relative_direction == 0:
                return(2)
            elif relative_direction == 1:
                return(3)
            elif relative_direction == 2:
                return(1)
            elif relative_direction == 3:
                return(0)

    def JE(self): #Jet
        def move():
            if direction == 0 and self.listpos > rows and not Board[self.listpos - rows]:
                Board[self.listpos].listpos = self.listpos - rows
                Board[self.listpos - rows] = Board[self.listpos]
                Board[self.listpos] = None
            elif direction == 1 and len(Board) - rows > self.listpos and not Board[self.listpos + rows]:
                Board[self.listpos].listpos = self.listpos + rows
                Board[self.listpos + rows] = Board[self.listpos]
                Board[self.listpos] = None
            elif direction == 2 and self.listpos % columns != columns - 1 and not Board[self.listpos + 1]:
                Board[self.listpos].listpos = self.listpos + 1
                Board[self.listpos + 1] = Board[self.listpos]
                Board[self.listpos] = None
            elif direction == 3 and self.listpos % columns != 0 and not Board[self.listpos - 1]:
                Board[self.listpos].listpos = self.listpos - 1
                Board[self.listpos - 1] = Board[self.listpos]
                Board[self.listpos] = None
            else:
                pass
        direction = self.determine_direction()
        move()

    def MO(self): #Mouth
        if Foods[self.listpos] != None:
            print(Foods[self.listpos])
            Foods[self.listpos] = None
            Board[self.listpos].energy += 1000
        else:
            pass