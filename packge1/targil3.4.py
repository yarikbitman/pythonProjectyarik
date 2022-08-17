from random import randint
num=int(input("enter number between 1 and 100: "))
count=0
while num>=1 and num<=100:
    num2=randint(1,100)
    count+=1
    if num==num2:
        print(count+1)
        break


