num=int(input("enter number: "))
for i in range(2,num):
    if num%i==0:
        print(f"{num} is nut first number")
        break
    else:
        print(f"{num} is first number")
        break

