len_const = 15
f = [1, 1]
# Do it with while
while len(f) < len_const:
    f.insert(len(f), f[len(f)-1]+f[len(f)-2])
print(f)
# Сlean changes in variables
f = [1, 1]
# Do it with for
for i in range(len_const-2):
    f.insert(len(f), f[len(f)-1]+f[len(f)-2])
print(f)