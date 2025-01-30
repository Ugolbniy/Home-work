# Write a function that returns `max(len(s), n)` characters from the middle of the string.
def middle(s: str, n: int) -> str:
    if n <= 0:
        return ""
    
    mid = len(s) // 2
    half_n = n // 2
    
    # Calculate the start and end indices to slice from the middle
    start = max(0, mid - half_n)
    end = min(len(s), mid + half_n + (n % 2))  # Adjust for odd length n
    
    return s[start:end]

# Do not change the below's code
if __name__ == "__main__":
    assert middle("abddcvbn", 4) == "ddcv"
    assert middle("abddcvbn", 3) == "ddc"
    assert middle("dcd", 5) == "dcd"
    assert middle("", 10) == ""
