def count_char(s: str, c: str) -> int:
    count = 0  # Initialize a counter
    for char in s:
        if char == c:
            count += 1  # Increment the counter each time 'c' is found
    return count

# Do not change the below's code
if __name__ == "__main__":
    assert count_char("ababa", "a") == 3
    assert count_char("ababa", "b") == 2
    assert count_char("ababa", "c") == 0
    assert count_char("cccca", "a") == 1
