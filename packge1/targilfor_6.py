grade=int(input("enter grade: "))
count1=0
count2=0
total1=0
total2=0
while grade<=100 and grade>=0:

    if grade>=60:
        count1+=1
        total1+=grade
    else:
        count2+=1
        total2 += grade
    grade = int(input("enter grade: "))
print(f"average grades: {total1/count1}")
print(f"average grades: {total2/count2}")