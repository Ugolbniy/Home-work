def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    assert is_even(2) is True
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(4) is True
