number = input('Print your number\n')

if number.isdigit() == 0:
    print('Wrong Data')
elif int(number) % 1000 == 0:
    print('Millennium')
else:
    print('Not Millennium')
