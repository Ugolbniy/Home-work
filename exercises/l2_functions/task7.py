def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    assert greet("Jon") == "Hello, Jon!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Baba") == "Hello, Baba!"
