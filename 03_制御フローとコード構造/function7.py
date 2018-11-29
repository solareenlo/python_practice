"""This is a test program."""
def outer(a, b):
    """関数内関数です"""
    def plus(c, d):
        """２数の和を返します"""
        return c + d
    r1 = plus(a, b)
    r2 = plus(b, a)
    return r1 + r2

s = outer(1, 2)
print(s) # 6 と表示
