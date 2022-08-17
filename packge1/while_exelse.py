grade=int(input("enter grade: "))
count_invalid=0
while grade>=0 and grade<=100:
    count_invalid+=1
    if count_invalid==5:
        break
    grade = int(input("enter grade: "))
else:
    print("error")