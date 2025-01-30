from pathlib import Path

L10_PATH = Path(__file__).parent

def write(path: Path, content: str):
    try:
        with open(path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"

    assert path.exists() is False
    write(path, text)
    assert path.exists() is True
    assert path.read_text() == text

    path.unlink(missing_ok=True)

a = 15
b = 3
quotient_result = a / b
print(quotient_result)

