"""This is a test program."""
seat: list = [] # 車のシートを用意
mini: int = 0 # 車のシートの最小数値
maxi: int = 5 # 車のシートの最大数値
print(mini <= len(seat) < maxi, len(seat)) # True 0と出力
seat.append('p') # シートに1人乗って来た
print(mini <= len(seat) < maxi, len(seat)) # True 1と出力
seat.append('p') # シートの2人目乗って来た
print(mini <= len(seat) < maxi, len(seat)) # True 2と出力
seat.append('p') # シートに3人目乗って来た
print(mini <= len(seat) < maxi, len(seat)) # True 3と出力
seat.append('p') # シートに4人目乗って来た
print(mini <= len(seat) < maxi, len(seat)) # True 4と出力
seat.append('p') # シートに5人目乗って来た
print(mini <= len(seat) < maxi, len(seat)) # False 5と出力
seat.pop(0) # シートから1人降りてった
print(mini <= len(seat) < maxi, len(seat)) # True 4と出力
