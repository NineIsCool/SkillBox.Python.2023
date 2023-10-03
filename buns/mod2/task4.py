try:
    num=int(input('Введите натуральное число:'))
    if num>=0:
        print(bin(num)[2:], oct(num)[2:], hex(num)[2:])
    else:
        raise ValueError('Invalid input')
except:
    print("Неверный ввод")
