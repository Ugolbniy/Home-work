from typing import Any

def getter(d: dict[str, Any], key: str) -> Any:
    try:
        return d[key]
    except KeyError:
        return None

if __name__ == "__main__":
    d = {"a": 42}

    assert getter(d["a"]) == 42
    assert getter(d["senseoflife"]) is None
