s = [1, 2, 3, 4, 5]
d = []
len_s = len(s)
iterator = 0
# Do it with while
while iterator < len_s:
    d.insert(iterator, s[(iterator + len_s + 1) % len_s])
    iterator = iterator + 1
print(d)
# Сlean variables
d = []
iterator = 0
# Do it with for
for i in s:
    d.insert(iterator, s[(iterator + len_s + 1) % len_s])
    iterator = iterator + 1
print(d)

