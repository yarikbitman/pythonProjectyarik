count=0
total=0
for i in range(6):
    num=int(input(f"enter number{i+1}: "))
    if num%2==0:
        total+=num
        count+=1
print(f"total: {total}")
print(f"average: {total/count}")