num = int(input("How many digits to generate in the fibonacci series? "))
a = 0
b = 1
number = ""
for i in range(num):
    number = number +str(b) + str(a) + " "
    b += 1
    a += 1
print(number)