# addMe

def addme(a: int, b: int) -> int:
    return a + b

def divMe(a: int, b: int) -> float:
    if b == 0:
        print("not possible")
        return None
    return a / b

# Subtract Me

def subMe(a: int, b: int) -> int:
    """Returns the difference of a and b (a - b)."""
    return a - b

# Multiply Me

def multMe(a: int, b: int) -> int:
    """Returns the product of a and b (a * b)."""
    return a * b
