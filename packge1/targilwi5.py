num=int(input("enter number: "))
while num>=10 and num<=99:
    if num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
        print("lucky number")
    num = int(input("enter number: "))
