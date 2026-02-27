val1 = int(input("enter 1st value:"))
val2 = int(input("enter 2nd value:"))
val3 = int(input("enter 3rd value:"))

if val1 == val2 and val2 == val3:
    print("Its Equilateral triangle")
elif val1 == val2 and val2 != val3:
    print("Its isocelese triangle")
elif val1 != val2 and val2 != val3:
    print("Its Scalene triangle")