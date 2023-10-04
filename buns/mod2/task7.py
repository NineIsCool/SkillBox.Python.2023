nums=input()
count_1=0
for num in nums:
    if num=='1':
        count_1+=1
if count_1==len(nums)-count_1:
    print('yes')
else:
    print('no')