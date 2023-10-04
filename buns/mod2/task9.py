str = input().lower()
vowels = "ауоыиэяюёе"
consonants="бвгджзйклмнпрстфхцчшщ"
count_v, count_c=0,0
for char in str:
    if char in vowels:
        count_v+=1
    if char in consonants:
        count_c+=1
print(count_v,count_c)