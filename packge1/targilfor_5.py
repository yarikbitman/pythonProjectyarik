grade=int(input("enter grade: "))
count=0
total=0
while grade<=100 and grade>=0:
    if grade>=60:
        count+=1
        total+=grade
    grade = int(input("enter grade: "))
print(f"average grades: {total/count}")