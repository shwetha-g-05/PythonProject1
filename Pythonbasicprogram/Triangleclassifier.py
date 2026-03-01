# val1 = int(input("enter 1st value:"))
# val2 = int(input("enter 2nd value:"))
# val3 = int(input("enter 3rd value:"))
#
# if val1 == val2 == val2 == val3:
#     print("Its Equilateral triangle")
# elif val1 == val2 and val2 != val3:
#     print("Its isocelese triangle")
# elif val1 != val2 and val2 != val3:
#     print("Its Scalene triangle")

def classify_triangle(a1,a2,a3):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                return"Equlilateral triangle "
            elif a==b or b==c or c==a:
                return "Isoselece teinagle"
            else:
                return "scalene triangel"
        else:
            print("Not a Triangle")

    else:
        print("Not avalid lenght")


a= float(input("Enter the first number :"))
b= float(input("Enter the second number :"))
c= float(input("Enter the third number :"))

c1 = classify_triangle(a,b,c)
print(c1)