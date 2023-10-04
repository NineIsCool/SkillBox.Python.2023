words = input()+' '
res_word = ''
for i in range(len(words)):
    if words[i] == ' ':
        res_word += words[i-1]
print(res_word)