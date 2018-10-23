from batleship import Battleship as bs
import os

os.system('clear')
player1 = bs()
player2 = bs()
print("Lets play battleship.\nHow wide of a board you want?")
x = int(input())
print("\nHow many ships do you want?\n")
y = int(input())
player1.create_board(x,y)
player2.create_board(x,y)
while True:
    os.system('clear')
    print("\n\n")
    player1.printer()
    print("\n\n")
    player2.printer()
    print("\n\nPlayer 1 take (a)nother shot")
    x = int(input("\n\nPick an x coordinate:  "))
    y = int(input("\n\nPick an y coordinate:  "))
    player1.shooter(x,y)
    if  player1.checker():
        break
    os.system('clear')
    print("\n\n")
    player1.printer()
    print("\n\n")
    player2.printer()
    print("\n\nPlayer 2 take (a)nother shot")
    x = int(input("\n\nPick an x coordinate:  "))
    y = int(input("\n\nPick an y coordinate:  "))
    player2.shooter(x,y)
    if  player2.checker():
        break
print("Congratz you have sunk the ship, you monster.")
    

