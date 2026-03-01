def sum_of_two_num(num1, num2=200):
    print("sum of 2 numbers id : ", num1+num2)

sum_of_two_num( 300)

def make_pizza(*Toppings):
    print(list(Toppings))
    for i in Toppings:
        print(i)

shwetha = make_pizza("Tamota", "corn")


def prod_of_3_num(num1=10,num2=30,num3=60):
    return num1*num2*num3

result = prod_of_3_num(2,3)
print(result)

result1 = prod_of_3_num(20)
print(result)