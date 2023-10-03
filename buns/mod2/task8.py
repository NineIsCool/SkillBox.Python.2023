str, symbol = input().split(',')
count = 0
for i in str:
    if i == symbol:
        count += 1
    else:
        break
print(count)