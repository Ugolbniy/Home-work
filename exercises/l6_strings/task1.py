# Write a function that returns a string where each word is reversed,
# but the word order remains the same.
def reverse_words(s: str) -> str:
    return ' '.join([word[::-1] for word in s.split()])

# Do not change the below's code
if __name__ == "__main__":
    assert reverse_words("hello world") == "olleh dlrow"
    assert reverse_words("python is fun") == "nohtyp si nuf"
    assert reverse_words("test") == "tset"
    assert reverse_words("a b c") == "a b c"
