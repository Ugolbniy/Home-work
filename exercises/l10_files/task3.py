from pathlib import Path

L10_PATH = Path(__file__).parent

def is_file(p: Path):
    try:
        return p.is_file()
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    path = L10_PATH / "example.txt"
    path.touch()

    assert is_file(path) is True
    assert is_file(L10_PATH) is False

    path.unlink(missing_ok=True)

a = 9
b = 4
modulus_result = a % b
print(modulus_result)
