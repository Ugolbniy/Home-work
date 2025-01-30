if __name__ == "__main__":
    # Do not modify the line below
    a, b = {"a", "b", "c", "d"}, {"a", "b", "n", "m"}

    c = a.union(b)  

    union_dict = {item: 1 for item in c}  
    # Do not modify the line below
    assert c == {"a", "b", "c", "d", "n", "m"}
