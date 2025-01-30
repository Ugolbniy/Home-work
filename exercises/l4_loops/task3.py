# Factorial using while loop
def factorial_while(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Factorial using for loop
def factorial_for(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Do not change the below's code
if __name__ == "__main__":
    assert factorial_while(2) == 2
    assert factorial_while(3) == 6
    assert factorial_while(4) == 24
    assert factorial_while(5) == 120
    assert factorial_while(6) == 720

    assert factorial_for(2) == 2
    assert factorial_for(3) == 6
    assert factorial_for(4) == 24
    assert factorial_for(5) == 120
    assert factorial_for(6) == 720
