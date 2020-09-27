exit_word = 'stop'
summa = 0
while True:
    user_string = input('Введи число\n')
    if not user_string.isdigit() and user_string.lower() != exit_word:
        print(f'Введи ЧИСЛО или STOP.Вы ввели {user_string}.')
    elif user_string == exit_word:
        print('Stoooooop')
        break
    else:
        summa = summa + int(user_string)
        print(summa)

