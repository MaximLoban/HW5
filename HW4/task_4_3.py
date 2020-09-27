d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Do it with for
for key in list(d.keys()):
    d[key + str(len(key))] = d[key]
    del d[key]
print(d)
# Сlean changes in variables
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Do it with while
list1 = list(d.keys())
len_list1 = len(list1)
iterator = 0
while iterator < len_list1:
    d[list1[iterator] + str(len(list1[iterator]))] = d[list1[iterator]]
    del d[list1[iterator]]
    iterator = iterator + 1
print(d)