age=int(input("enter age: "))
if age>=0 and age<=18:
    print("child")
elif age>18 and age<=60:
    print("adult")
elif age>60 and age<=120:
    print("senior")