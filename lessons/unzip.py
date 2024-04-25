"""Splitting a dictionary into two lists."""

__author__ = "730567934"


def get_keys(in_stock: dict[str, int]) -> list[str]:
    """List of all the keys in the input dictionary."""
    list_key = []
    for key in in_stock:
        list_key.append(key)
    return list_key
        

def get_values(in_stock: dict[str, int]) -> list[int]:
    """List of all the values in the input dictionary."""
    list_values = []
    for value in in_stock:
        list_values.append(in_stock[value])
    return list_values
