def count_positive(n: list[int]) -> int:
    count = 0
    # Iterate through the list and count positive numbers
    for num in n:
        if num > 0:
            count += 1
    return count

# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4
