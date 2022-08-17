num1=int(input("enter grade: "))
# if num1>=0 and num1<=100:
#     if num1>=70:
#         print("pass")
#     else:
#         print("fails")
# else:
#     print("error")
while num1>100 or num1<0:
    print("invalid grade. must be 100-0")
    num1 = int(input("enter grade: "))
if num1>70:
    print("pass")
else:print("error")
