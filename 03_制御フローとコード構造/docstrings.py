"""This is a test program."""
def example_func(param1, param2):
    """Exammple function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
     """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__) # 上記の""""""の中身が表示される

help(example_func) # 上記の""""""の中身が表示されて, helpに入る
