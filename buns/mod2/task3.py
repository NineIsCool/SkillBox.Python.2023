data_input=input()+' '
a, b, c = "","",""
cur_num=""
for char in data_input:
    if char == ' ':
        if a=="":
            a = cur_num
        elif b=="":
            b=cur_num
        else:
            c=cur_num
        cur_num = ""
        continue
    cur_num += char
a,b,c=int(a),int(b),int(c)
if a>b:
    if a<c:
        print(a)
elif c>b:
    print(b)
else:
    print(c)