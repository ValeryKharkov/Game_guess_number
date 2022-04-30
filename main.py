print('Добро пожаловать в числовую угадайку!')
print('Угадайте число от 1 до 100, загаданное программой.')

import random
random_int = random.randint(1, 100)
# print('random_int =', random_int)  # Печать рандомного числа для проверки


def is_valid(arg_: str) -> bool:
    if arg_.isdigit() and 0 <= int(arg_) <= 100:
        return True
    else:
        return False


def is_num_in_range(user_number: int, random_number: int) -> str:
    if user_number == random_number:
        return 'Вы угадали, поздравляем!'
    elif user_number < random_number:
        return 'Слишком мало, попробуйте еще раз'
    elif user_number > random_number:
        return 'Слишком много, попробуйте еще раз'


while True:
    user_int = input('{blue}Введите число: {endcolor}'.format(blue='\033[96m', endcolor="\033[0m"))
    if is_valid(user_int):
        print(is_num_in_range(int(user_int), random_int))
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
