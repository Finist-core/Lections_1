print('Как тебя зовут?')
name = input()
print('Привет', name)
print('Сколько тебе лет?')
age = int(input())
print('А я думал тебе', age + 1, end = '')
age = age + 1
if 19 >= age >= 11:
    print(' лет')
elif age % 10 == 1:
    print(' год')
elif age % 10 >= 2 and age % 10 <= 4:
    print(' года')
else:
    print(' лет')


