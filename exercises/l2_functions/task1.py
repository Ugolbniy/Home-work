Number = int | float | complex

def sqr(n: Number) -> Number:
    return n * n  # or n ** 2

if __name__ == "__main__":
    # Do not change the below asserts
    assert sqr(2) == 4
    assert sqr(4.0) == 16
    assert sqr(3 + 2j) == 5 + 12j
