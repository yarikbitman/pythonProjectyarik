num=int(input("enter number: "))
if num>=10 and num<=99:
    if num%7==0 or num%10==7 or num//10==7:
        print("lucky number")
else:
    print("error")
