data_input=input()
a,b="",""
cur_domen=""
for char in data_input:
    if char == '.':
        if a=="":
            a = cur_domen
        elif b=="":
            b=cur_domen
        else:
            c=cur_domen
        cur_domen = ""
        continue
    cur_domen += char
print(a)
print(b)
print(cur_domen)