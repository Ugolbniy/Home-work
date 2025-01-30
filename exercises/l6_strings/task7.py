# Write a function that returns a string with all the vowels removed.
def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

# Do not change the below's code
if __name__ == "__main__":
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("world") == "wrld"
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("TESTING") == "TSTNG"
