from pathlib import Path

L10_PATH = Path(__file__)

def path_exists(path: str) -> bool:
    try:
        return (L10_PATH.parent / path).exists()
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    assert path_exists(".") is True
    assert path_exists("../__init__.py") is True
    assert path_exists("../task1.py") is True
    assert path_exists("../wrong.txt") is False
    assert path_exists("/wrong/path") is False

a = 8
b = 4
division_result = a / b
print(division_result)
