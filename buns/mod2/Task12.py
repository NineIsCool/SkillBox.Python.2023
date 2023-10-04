phone_number = input()
no_correct_symbols="-() "
res_phone=""
for num in phone_number:
    if not(num in no_correct_symbols):
        res_phone+=num
print(res_phone)