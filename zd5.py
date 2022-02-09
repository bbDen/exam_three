n = int(input('Введите число '))

summa = 0


while n > 0:
    digit = n % 10
    summa = summa + digit
    n = n // 10

print(f'Сумма {summa}')
