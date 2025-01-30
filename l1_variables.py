if __name__ == "__main__":
    # Multiple assignment
    i = j = a = b = 0

    # Immutable and Mutable
    a = 4

    # All simple types are immutable:
    # - None
    # - bool
    # - int
    # - float
    # - complex
    # - tuple
    # - str

    tr = True
    fl = False

    i = 9  # int
    p = 9.2  # float
    c = 3 + 1j

    # Strings

    # 1. use ''
    s = "text of str"

    # 2. use ""
    s = "text of str"

    # 3. use ''' ''' or """ """
    # s = """
    # text of str.

    # new line.
    # """
    print(s)
    print(s[2])

    # This will throw an error because
    # str is immutable
    # s[2] = "c"

    # Tuple - Кортеж
    a = ("str", 3, 3.5, True)
    print(a)
    print(a[1])
    print(type(a))

    tup = "str", 6, 6.5, False
    print(tup)
    print(type(tup))

    # Usual mistake of Python devs
    # i = 0,
    # print(i + 10)

    # Empty tuple
    n = ()  # There is only one copy of empty tuple () in memory
    print(type(n))

    # This will throw an error because
    # tuple is immutable
    # a[0] = 10

    # Mutable types are the rest of types
    l = [1, 2, 3, 4, 5]
    print(l)
    print(l[0])

    l[0] = 10
    print(l)

    # Expanding of collections
    p = (3.0, 4.1)

    print(p[0], p[1])
    print(p[1], p[0])

    x, y = 3.0, 5.1
    print(x)
    print(y)

    # Type casting
    x = 10  # int
    y = 0.5  # float
    z = x + y
    print(type(z), z)

    # Case of error
    # x = "10"
    # y = 10
    # z = x + y  # error is here
    x = "10"
    y = float(x)
    print(type(y), y)

    # y = int("fewhufhweu") # error is here
    print(str(y))
    print(str(p))
    print(str(print))

    # Math
    a = 10 + 10 - 10 * 1 / 10  # Basic math operations
    c = 20 % 5  # modulo; period
    d = 10**2  # exp
    e = 10 // 3  # integer division

    i = 0
    i = i + 1
    i += 1
    # i++  # Error in Python

    i -= 1
    i *= 1
    i /= 1
    i **= 1
    i %= 1

    b = True
    n = False

    c = b and n
    c = b or n
    c = b and not n

    # Type hinting or type annotation
    j: int = 1
    j: str
