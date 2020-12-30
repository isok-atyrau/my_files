tr = []

##for i in range(n+1):
##    tr.append([1] + [0] * n)
##
##for i in range(1, n+1):
##    for j in range(1, i+1):
##        tr[i][j] = tr[i-1][j] + tr[i-1][j-1]
##
##for i in range(0, n+1):
##    for j in range(0, i+1):
##        print(tr[i][j], end=' ', )
##    print()

##a = [2,5,7,5,9,2,3,4,2,5]
##
##count = [0]*10
##for i in a:
##    count[i] += 1
##for i in range(10):
##    if count[i] > 0:
##        print((str(i) + ' ') * count[i], end='')

##d = {}
##
##s = "akkkAFA"
##for i in s.lower():
##    if i.isalpha():
##        d[i] = d.get(1, 0) +1
####        if i in d:
####            d[i] += 1
####        else:
####            d[i] = 1
##for i in d:
##    print(i, d[i])
import random

secret = random.randint(1, 50)

# инициализируем переменную guess
guess = -1
# в переменной attempt будем хранить счетчик использованных пользователем попыток
attempt = 0
# пока предположение пользователя не совпадает с секретом
while guess != secret:
    # просим пользователя ввести очередное предположение и сохраняем его в переменную
    guess_string = input('Угадай загаданное число: ')
    # приводим значение к типу int
    guess = int(guess_string)
    # увеличиваем на единицу счетчик попыток
    attempt += 1
    # проверяем результат и распечатываем пользователю подсказку
    if guess < secret:
        print('Я загадал число больше, попробуй еще раз.')
    elif guess > secret:
        print('Я загадал число меньше, попробуй еще раз.')
# выход из цикла означает, что guess == secret поздравляем пользователя и указываем количество использованных попыток
print('Верно! Количество использованных попыток: ', attempt)
print(f'Ваш личный рекорд {attempt} попыток ')


