import model as mod
from random import shuffle



winniing_door = 0 
same_choice_victories = 0 
changed_choice_victories = 0

def choice1(x):
    doras = [1,2,3]
    shuffle(doras)
    winning_door = doras[0]
    doors = [1,2,3]
    doors.remove(winning_door)
    if x == doors[0]:
        picks2.remove(doors[1])
    elif x == doors[1]:
        picks2.remove(doors[0])
    else:
        picks2.remove(doors[0])
        #print("Okay so in door {} there is a goat.\n\nWhat door do you pick now?".format(show))
    
def choice2(y):
    if y == winning_door:
        #print("Congratulations you win a car!")
        return(True)
    else:
        #print("CONGRATULATIONSSSSSSSSSSSSSS YOU WIN A goat.")
        return(False)
    


for i in range(0,10):
        
        picks1 = [1,2,3]
        shuffle(picks1)
        picks2 = [1,2,3]
        choice1(picks1[0])
        shuffle(picks2)
        if picks1[0] == picks2[0] and choice2(picks2[0]):
            same_choice_victories += 1 
        elif picks1[0] == picks2[0] and choice2(picks2[0]):
            changed_choice_victores += 1 

        
print(same_choice_victories)

    
