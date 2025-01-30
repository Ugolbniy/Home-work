from pathlib import Path

L10_PATH = Path(__file__).parent

def read(path: Path) -> str:
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

if __name__ == "__main__":
    text = "Hello World!"
    path = L10_PATH / "example.txt"
    path.write_text(text)

    assert read(path) == text

    path.unlink(missing_ok=True)

a = 12
b = 7
difference_result = a - b
print(difference_result)
