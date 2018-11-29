"""This is a test program."""
def add_num(a: int, b: int) -> int:
    """2つの数の和を返します"""
    return a + b

r: int = add_num(10, 20)
print(r) # 30 と表示

r = add_num('a', 'b')
print(r) # ab と表示される. 上ではa, bはint型と宣言したけど, 御構い無しにstr型でも返してくれる.
