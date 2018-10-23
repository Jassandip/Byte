import time
import model as mod





def choice(x):
    winning_door = mod.winning_door()
    doors = [1,2,3]
    doors.remove(winning_door)
    if x == doors[0]:
        show = doors[1]
    elif x == doors[1]:
        show = doors[0]
    else:
        show = doors[0]
    print("Okay so in door {} there is a goat.\n\nWhat door do you pick now?".format(show))
    y = input()
    if y == winning_door:
        print("Congratulations you win a car!")
    else:
        print("CONGRATULATIONSSSSSSSSSSSSSS YOU WIN A goat.")
        
    print(x)


