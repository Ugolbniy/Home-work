# Write the body of the function to make it
# return a min value of dictionary `d`
def min_value(d: dict[str, int]) -> int:
    # Task on Dicts: Get the minimum value from the dictionary
    return min(d.values())  


    values_set = set(d.values())  
    return min(values_set)

# Do not change the below's code
if __name__ == "__main__":
    assert min_value({"a": 3, "b": 5}) == 3
    assert min_value({"a": 10}) == 10
    assert min_value({"a": -1, "b": -1, "default": 1}) == -1
