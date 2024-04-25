"""Ex05 - Practice with dictionary functions!"""

__author__ = "730567934"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the input."""
    inverted: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in inverted:
            raise KeyError
        inverted[value] = key
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    count: dict[str, int] = {}
    for color in colors.values():
        count[color] = count.get(color, 0) + 1

    max = 0
    most_frequent = ""
    for color, freq in count.items():
        if freq > max:
            max = freq
            most_frequent = color
    return most_frequent


def count(List: list[str]) -> dict[str, int]:
    """Retruns the times the value has repeated in the list."""
    value: dict[str, int] = {}
    for item in List:
        if item in value:
            value[item] += 1
        else:
            value[item] = 1
    return value


def alphabetizer(List: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    count: dict[str, list[str]] = {}
    for word in List:
        first_alphabet = word[0].lower()
        if first_alphabet in count:
            count[first_alphabet].append(word)
        else:
            count[first_alphabet] = [word]
    return count


def update_attendance(attend: dict[str, list[str]], day: str, name: str) -> None:
    """Mutates and returns that dictionary."""
    if day in attend:
        if name not in attend[day]:
            attend[day].append(name)
    else:
        attend[day] = [name]