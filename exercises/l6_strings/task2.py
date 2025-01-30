# Write a function that returns the last `max(len(s), n)` characters of string `s`.
# If `n <= 0`, return an empty string.
def take_last(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return s[-min(len(s), n):]

# Do not change the below's code
if __name__ == "__main__":
    assert take_last("abcde", 2) == "de"
    assert take_last("bbhj", 3) == "bhj"
    assert take_last("bjk", 0) == ""
    assert take_last("bjk", -1) == ""
    assert take_last("bjk", 100) == "bjk"
