nums=input().replace(' ','')
nums=''.join(sorted(nums))
fl=False
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        fl=True
        break
print(fl)

