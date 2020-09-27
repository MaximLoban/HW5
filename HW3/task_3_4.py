string = input('Print your string\n')
central_index = round(len(string) / 2)

print(string[central_index])

if string[central_index] == string[0]:
    b = string[1:len(string) - 1]
    print(b)

