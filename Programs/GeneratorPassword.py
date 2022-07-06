import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
amount = int(input('Количество паролей для генерации?'))
length = int(input('Длинa одного пароля?'))
q1 = input('Включать ли цифры 0123456789? (д/н)')
q2 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д/н)')
q3 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д/н)')
q4 = input('Включать ли символы !#$%&*+-=?@^_? (д/н)')
q5 = input('Исключать ли неоднозначные символы il1Lo0O? (д/н)')
if q1 == 'д':
    chars+=digits
if q2 == 'д':
    chars += uppercase_letters
if q3 == 'д':
    chars+= lowercase_letters
if q4 == 'д':
    chars+= punctuation
if q5 == 'д':
    for c in 'il1Lo0O':
        chars.replace(c, '')
def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

for j in range(amount):
    print(generate_password(length, chars))