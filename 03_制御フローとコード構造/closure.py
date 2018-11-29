"""This is a test program."""
def circle_area_func(pi):
    """closureの例"""
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10)) # 314.0 と表示
print(cal2(10)) # 314.1492 と表示

# closureとは関数の2段構えにおいて, 2つの関数の実行のタイミングを違えるということ
