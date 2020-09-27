# Declare variables
string_qty = 9
symbol = '* '
# Create list with positive numbers
list_of_numbers = [i+1 for i in range(string_qty)]
# Find middle string
middle_string = round(string_qty/2)

max_qty = middle_string
for i in list_of_numbers:
    if i <= max_qty:
        print(symbol*i)
    elif i > max_qty:
        print(symbol * abs(i-string_qty-1))
