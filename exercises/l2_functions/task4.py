from typing import Iterable

def my_len(iterable: Iterable) -> int:
    return len(iterable)

if __name__ == "__main__":
    assert my_len([3, 4, 5]) == 3
    assert my_len("abv") == 3
    assert my_len({"a": 1, "b": 3}) == 2
    assert my_len((3, 4, 5)) == 3
