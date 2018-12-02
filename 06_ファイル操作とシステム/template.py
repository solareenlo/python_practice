import string # $xxxに文字列を代入するための標準ライブラリ

s = """\
Hi $name.
$contents
Have a good day
"""

t = string.Template(s) # .Templateは読み込み専用
contents = t.substitute(name='Mike', contents='How are you?') # 上記のsの$nameにMikuを, $contentsにHow are you? を代入
print(contents) # Hi Mike. How are you? Have a good day と縦に表示

with open('design/email_template.md') as f: # 別ファイルにある内容をとって来る.
    t = string.Template(f.read()) # .Templateは読み込み専用
contents = t.substitute(name='Mike', contents='How are you?')
print(contents) # Hi Mike. How are you? Have a good day と縦に表示
