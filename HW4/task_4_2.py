list1 = [1, 3, -10, 12, 2, 5, 6, 8, - 8, -1]
list1_len = len(list1)
qty_ = 0
iterator = 0
# Do it with while
while iterator < list1_len:
    if list1[iterator] % 2 == 0:
        qty_ = qty_ + 1
    iterator = iterator + 1
print(qty_)
# Сlean variables
qty_ = 0
iterator = 0
# Do it with for
for i in list1:
    if list1[iterator] % 2 == 0:
        qty_ = qty_ + 1
    iterator = iterator + 1
print(qty_)
