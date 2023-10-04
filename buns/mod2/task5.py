import binary_search_str

data_input=input()
i=binary_search_str.binary_search(data_input,',')
symbol=data_input[:i]
offset=int(data_input[i+1:])
alph='abcdefghijklmnopqrstuvwxyz'
print(alph[(binary_search_str.binary_search(alph,symbol)+offset)%26])
