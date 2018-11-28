"""This is a test program."""
def say_something(): # functionは直ぐ下に説明文が必要みたいです
    """stringを返します"""
    say = 'hi'
    return say

result: str = say_something()
print(result)

def what_is_this(color):
    """色に対するものを返します"""
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result: str = what_is_this('red')
print(result)
result: str = what_is_this('green')
print(result)
result: str = what_is_this('yellow')
print(result)
