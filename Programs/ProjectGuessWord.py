import random
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    if (num.isdigit() == True) and ((int(num) >= 1) and (int(num) <= q)):
        return True
    else:
        return False

def max_range():
    while True:
        n = input('\nМаксимальное число? ')
        if not n.isdigit() or int(n) < 1:
            print('Введите целое число больше нуля!')
            continue
        return int(n)
q = max_range()
num = random.randint(1, q)
def continue_game():
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True
def game():
    count = 0
    while True:
        n = input(f'Введите число от 1 до {q}:')
        count += 1
        if is_valid(n) == True:
            n = int(n)
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n == num:
                print('Вы угадали, поздравляем! Количество попыток:', count)
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {q}?')
            continue
game()







