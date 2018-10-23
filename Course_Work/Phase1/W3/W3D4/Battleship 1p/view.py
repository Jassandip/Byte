from batleship import Battleship as bs
import os

os.system('clear')
player = bs()
print("Lets play battleship.\nHow wide of a board you want?")
x = int(input())
print("\nHow many ships do you want?\n")
y = int(input())
player.create_board(x,y)
os.system('clear')
while True:
    player.printer()
    print("\n\nTake (a)nother shot")
    x = int(input("\n\nPick an x coordinate:  "))
    y = int(input("\n\nPick an y coordinate:  "))
    player.shooter(x,y)
    if  player.checker():
        break
    os.system('clear')
print("Congratz you have sunk the ship, you monster.")

