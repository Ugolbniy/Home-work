from pathlib import Path

L10_PATH = Path(__file__).parent

def create_directory(name: str):
    try:
        (L10_PATH / name).mkdir()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    name = "tmp"
    path = L10_PATH / name
    assert path.exists() is False

    create_directory(name)
    assert path.exists() is True
    path.rmdir()

a = 6
b = 3
product_result = a * b
print(product_result)
