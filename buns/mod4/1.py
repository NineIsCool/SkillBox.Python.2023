def characteristic_lst(lst):
    if len(set(lst))==len(lst):
        return "Все числа разные"
    if lst.count(lst[0])== len(lst):
        return "Все числа равны"
    return "Есть равные и неравные числа"

print(characteristic_lst([2,2,2,2]))