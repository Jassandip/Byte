import pprint
from random import shuffle 

class Battleship:
    def __init__(self):
        self.d = []
        self.ships = 0
        self.sunk = 0
        self.winning_numbers = {} 
    
    def create_board(self,x,y):
        bar = list(range(1,(x*x)+1))   # creates a random list and shuffles it 
        shuffle(bar)
        self.ships = y
        for i in range(y):  # creates as many ships as the player inputs he/she wants 
            winning_index = ((bar.pop())-1)   # chooses the highest number from the list shuffled above and uses its index as the spot for the shi[]
            a = winning_index // x   # this decalers that a winning Y coordinate will be "a"
            b = winning_index % x    # this decalers that a winning X coordinate will be "b"  
            self.winning_numbers[str(b)]=str(a)
        self.d = []   # this will be my list of lists that will hold the starting clean board
        for i in range(0,x):
                i = []
                for j in range(0,x):
                    i.append('O')
                self.d.append(i)
        
    def shooter(self,x,y):
        if (str(x - 1),str(y - 1)) in self.winning_numbers.items(): 
            print("BOOOOM your shot landed")
            self.d[y-1][x-1] = "X"
            self.sunk += 1
        else:
            self.d[y-1][x-1] = "#"  # replaces the "O" with "X" so you know you already fired there.

    def printer(self):
        for i in self.d:
            print(" ".join(i)) 

    def checker(self):
        if self.sunk == self.ships:
            return True

    





        
