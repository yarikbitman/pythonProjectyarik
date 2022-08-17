num1=int(input("enter number: "))
num2=num1%10
num3=num1//10%10
num4=num1//100
while num1<=999 and num1>=100:
    print(num2 + num3 + num4)

    num1 = int(input("enter number: "))
