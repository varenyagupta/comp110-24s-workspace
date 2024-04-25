"""EX04 - List Utility Function."""

author = "73056793"

    
def all(list: list[int], num: int) -> bool: 
    """Checking if the integers in the list are equal or not."""
    i: int = 0 
    if len(list) == 0: 
        return False 
    for i in range(len(list)):
        if list[i] != num:
            return False
    i += 1
    return True 


def max(num: list[int]) -> int:
    """Checking for the max number in the list."""
    if len(num) == 0:
        raise ValueError("max() arg is an empty List")
    max = num[0]
    i: int = 0 
    for i in range(len(num)):
        if num[i] > max: 
            max = num[i]
    i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checking if there is an integer equal in the lists."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    for i in range(len(list1)):
        if list1 != list2:
            return False
    i += 1 
    return True 


def extend(list1: list[int], list2: list[int]) -> None:
    """Appending last integer of list 2 to list 1."""
    for item in list2:
        list1.append(item)