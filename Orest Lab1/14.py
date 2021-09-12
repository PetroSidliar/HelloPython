power = int(input("Enter power: "))
raised = 2**power
x = raised
x_string = str(x)
x_length = len(x_string)
c = int(x_string[x_length - 2: x_length])
print("The last two digit for the number: ", x, " is: ", c)
