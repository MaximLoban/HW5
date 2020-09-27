string = input('Print your string\n')

if len(string) < 10:
    b = string + '!!!'
    print(b)
# print(f'{string}!!!')
elif len(string) > 10:
    print(string[2])
else:
    print('10 symbols')
