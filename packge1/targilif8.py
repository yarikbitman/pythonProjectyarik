day=int(input("enter day: "))

if day>=1 and day<=31:
    month = int(input("enter month: "))
    if month>=1 and month<=12:
        year = int(input("enter year: "))
        if year>=1950 and year<=2022:
            # y1=year//10%10
            # y2=year%10
            # print(f"{day}/{month}/{y1}{y2}")
            print(f"{day}/{month}/{year//10%10}{year%10}")
        else:
            print("invalid year!!!")
    else:
        print("invalid month!!!")
else:
    print("invalid day!!!")




