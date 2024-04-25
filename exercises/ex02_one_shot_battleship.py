"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730567934"

grid_size: int = 4
secret_row: int = 3
secret_col: int = 2 
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


user_row: int = int(input("Guess a row: "))
while user_row > grid_size or user_row < 1: 
    user_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

user_col: int = int(input("Guess a column: "))
while user_col > grid_size or user_col < 1: 
    user_col = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))    

result_box: str = ""
if secret_row == user_row and secret_col == user_col:
    result_box = RED_BOX
else: 
    result_box = WHITE_BOX

row_count: int = 1 
while row_count <= grid_size:
    emoji: str = ""
    col_count: int = 1 
    if user_row == row_count:
        while col_count <= grid_size:
            if user_col == col_count: 
                emoji += result_box
            else:
                emoji += BLUE_BOX
            col_count += 1 
    else:
        while col_count <= grid_size:
            emoji += BLUE_BOX
            col_count += 1 
    print(emoji)
    row_count += 1 

if secret_row == user_row and secret_col == user_col:
    print("Hit!")
elif secret_col == user_col and secret_row != user_row:
    print(" Close! Correct column, wrong row.")
elif secret_col != user_col and secret_row == user_row:
    print(" Close! Correct row, wrong column.")
else:
    print("Miss!")
