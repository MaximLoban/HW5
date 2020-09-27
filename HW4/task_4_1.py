list1 = [1, 3, 12, 5, 6, 8, - 8, -1]
list1_len = len(list1)
list2 = []
iterator = 0
# Do it with while
while iterator < list1_len:
    list2.append(list1[iterator]*(-2))
    iterator = iterator + 1
print(list2)
# Clean variables
list2.clear()
iterator=0
# Do it with for
for i in list1:
    list2.append(list1[iterator] * (-2))
    iterator = iterator + 1
print(list2)