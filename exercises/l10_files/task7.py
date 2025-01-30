from pathlib import Path

L10_PATH = Path(__file__).parent

def count_lines(path: Path) -> int:
    try:
        with open(path, 'r') as file:
            return len(file.readlines())
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    text = "line\nline\nline\nline"
    path = L10_PATH / "example.txt"

    path.write_text(text)
    assert count_lines(path) == 4
    path.unlink(missing_ok=True)

a = 20
b = 4
power_result = a ** b
print(power_result)
