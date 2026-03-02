#using set

lst = [1,3,3,4,4,2,2,2]
lst1 =set(lst)
print(lst1)



#using loop
a = [1,3,3,4,4,2,2,2]
result =[]

for value in a:
    if value not in result:
        result.append(value)

print(result)

#using dict.formkeys()

lst = [1,3,3,4,4,2,2,2]
lst1 =list(dict.fromkeys(lst))
print(lst1)
