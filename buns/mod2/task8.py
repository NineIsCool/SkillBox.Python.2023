data_input=input()
symbol=data_input[len(data_input)-1:]
str=data_input[:len(data_input)-2]
count = 0
for i in str:
    if i == symbol:
        count += 1
    else:
        break
print(count)