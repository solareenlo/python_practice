"""This is a test program."""
count: int = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done!') # while文がbreakで抜けなければdone!が表示される. 今回はbreakで抜けたので, done!は表示されない
# while文のelseはbreakで抜けなければ実行される
