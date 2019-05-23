import pygame

from neuron_full import NeuronDo

#['type(2)', 'xyz', 'range(3)', tag(2)', 'bias', 'threshold', properties(4)', 'op1'(3), 'op2'(3), etc.]

INPUT = ('EY', 'EY')
OUTPUT = ('JE', 'MO')

class NeuralNet():
    def __init__(self, neurons):
        self.neurons = neurons
        self.next_move = pygame.time.get_ticks() + 100

    def neuron_check(self, listpos):
        for neuron in self.neurons:
            finalweight = neuron[4] #bias
            for neuron1 in self.neurons:
                if neuron != neuron1:
                    pass
                else:
                    pass
            if finalweight > neuron[5] and neuron[0] in OUTPUT:
                if pygame.time.get_ticks() >= self.next_move:
                    self.execute(neuron, listpos)
                    self.next_move = pygame.time.get_ticks() + 100

    def execute(self, neuron, listpos):
        NeuronDo(neuron, listpos)


    