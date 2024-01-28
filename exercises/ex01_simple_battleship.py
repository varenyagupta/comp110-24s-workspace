"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = 730567934

user_number: int = int(input("Pick a secret boat location between 1 and 4:"))
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if user_number < 1:
    print("Error!", str(user_number), "too low")
    exit()
else:
    if user_number > 4:
        print("Error!", str(user_number), "too high")
        exit()

player_number: int = int(input("Guess a number between 1 and 4:"))

if player_number < 1:
    print("Error!", str(player_number), "too low")
    exit()
else:
    if player_number > 4:
        print("Error!", str(player_number), "too high")
        exit()

emoji = " "

if player_number == 1:
    emoji += RED_BOX if user_number == 1 else WHITE_BOX
else:
    emoji += BLUE_BOX

if player_number == 2:
    if emoji == BLUE_BOX:
        emoji = " "
    emoji += RED_BOX if user_number == 2 else WHITE_BOX
else:
    emoji += BLUE_BOX

if player_number == 3:
    if emoji == BLUE_BOX * 2:
        emoji = " "
    emoji += RED_BOX if user_number == 3 else WHITE_BOX
else:
    emoji += BLUE_BOX

if player_number == 4:
    if emoji == BLUE_BOX * 3:
        emoji = " "
    emoji += RED_BOX if user_number == 4 else WHITE_BOX
else:
    emoji += BLUE_BOX

print(emoji)

if user_number == player_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")





 
      
    