data_input = input().replace(' ','')
a,b="",""
cur_num=""
for char in data_input:
    if char==',':
        if a=="":
            a=cur_num
        else:
            b=cur_num
        cur_num=""
        continue
    cur_num+=char
b=cur_num
print(float(a) % float(b))