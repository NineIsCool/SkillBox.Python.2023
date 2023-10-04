try:
    num=int(input())
    if num>=0:
        print(f'{num:b}',', ', f'{num:o}', ', ', f'{num:x}')
    else:
        raise ValueError('Invalid input')
except:
    print("Неверный ввод")
