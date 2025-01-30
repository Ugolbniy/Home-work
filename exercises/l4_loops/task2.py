def odd_str(n: int) -> str:
    s = ""

    # Use for loop to run from 0 to n (included) 
    # and form a string `s` with only odd numbers.
    for i in range(n + 1):
        if i % 2 != 0:
            s += str(i)
    
    return s


# Do not change the below's code
if __name__ == "__main__":
    assert odd_str(4) == "13"
    assert odd_str(6) == "135"
    assert odd_str(8) == "1357"
