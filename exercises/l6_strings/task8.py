# Write a function that formats a string in a specific way
def you_are(s: str) -> str:
    return f"You are {s}"

# Do not change the below's code
if __name__ == "__main__":
    assert you_are("Jon") == "You are Jon"
    assert you_are("Sansa") == "You are Sansa"
    assert you_are("Cersei") == "You are Cersei"
