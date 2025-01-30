def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        n //= 10  # Integer division by 10 removes the last digit
        count += 1
    return count if count > 0 else 1  # Special case for 0

# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
