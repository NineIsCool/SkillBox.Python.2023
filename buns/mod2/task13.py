barcode=input()
switch=True
sum = 0
for num in barcode:
    if switch:
        sum+=int(num)
        switch=False
    else:
        sum += int(num) * 3
        switch=True
if sum%10==0:
    print('yes')
else:
    print('no')