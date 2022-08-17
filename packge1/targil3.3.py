from random import randint
num=randint(1,9)
num2=int(input("enter number between 1 and 9: "))
while num2>0 and num2<10:
    if num==num2:
        print("good for you!!!")
        break
    elif num>num2:
        print("your number is smaller then the computer try agen ")
    elif num<num2:
        print("your number is bigger then the computer number try agen")
    num2 = int(input("enter number between 1 and 9: "))