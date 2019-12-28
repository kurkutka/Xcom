import random
from move import Move

class Ai:
    def ai(self,choise_allien, spis):
        for elem in choise_allien:
            if elem[2] == 'sectoid':
                ss = []
                for y in range(9):
                    for x in range(9):
                        ss.append([elem[0] - 4 + y][elem[1] - 4 + x])
                for elem

