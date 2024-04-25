"""Writing A Recursive Function."""


def f(n: int, k: int) -> int:
    """Recursive defination."""
    if n == 0:
        return 0 
    else:
        return f(n - 1, k) + k
    
    
print(f(2, 2)) 
print(f(3, 4)) 
print(f(5, 4))