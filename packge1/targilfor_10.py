num1=int(input("enter number: "))
count=0
count1=0
while num1!=0:
    if num1%7==0:
        count+=1
    elif num1%3==0:
        count1+=1
    num1 = int(input("enter number: "))
print(f"{count+count1} dividing in 3 or 7")