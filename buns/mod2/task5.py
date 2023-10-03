symbol, offset = input().split(",")
alph='abcdefghijklmnopqrstuvwxyz'
offset = (int(offset))
print(alph[(alph.find(symbol)+offset)%26])
