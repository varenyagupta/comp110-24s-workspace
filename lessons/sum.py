"""Summing the elements of a list using different loops."""

author = "730567934"


def w_sum(vals: list[float]) -> float:
    """Finding sum using while loops."""
    sum_val = 0.0
    i = 0
    while i < len(vals):
        sum_val += vals[i]
        i += 1
    return sum_val


def f_sum(vals: list[float]) -> float:
    """Finding sum using for loop."""
    sum_val = 0.0
    for val in vals:
        sum_val += val
    return sum_val


def f_range_sum(vals: list[float]) -> float:
    """Find using for loop but using range."""
    sum_val = 0.0
    for i in range(len(vals)):
        sum_val += vals[i]
    return sum_val