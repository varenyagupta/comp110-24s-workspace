"""EX03 - Funcitonal Battleship."""

__author__ = "730567934"

import random


def input_guess(grid_size: int, place: str) -> int:  
    """Taking user guess."""
    assert place == "row" or place == "column"
    user_guess: int = int(input(f"Guess a {place}: "))
    while user_guess > grid_size or user_guess < 1: 
        user_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return user_guess


def print_grid(grid_size: int, row_guess: int, col_guess: int, guess: bool) -> None:
    """Creating a grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = ""
    if guess is True:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX
    row_count: int = 1 
    while row_count <= grid_size:
        emoji: str = ""
        col_count: int = 1 
        if row_guess == row_count:
            while col_count <= grid_size:
                if col_guess == col_count: 
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


def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Checking if the guess is correct."""
    return secret_row == row_guess and secret_col == col_guess


def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Assembling all functions."""
    turn_count: int = 1
    while turn_count < 6:
        print(f"===Turn {turn_count}/5===")
        user_row = input_guess(grid_size, "row")
        user_col = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_col, user_row, user_col)
        print_grid(grid_size, user_row, user_col, correct)
        if correct:
            print(f"Hit! You won in {turn_count}/5 turns!")
            return
        else:
            print("Miss!")
        turn_count += 1
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))