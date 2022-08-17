count=0
total=0
for i in range(6):
    count+=1
    num=int(input(f"enter number{i+1}: "))
    total+=num
print(f"total: {total}")
print(f"average: {total/count}")