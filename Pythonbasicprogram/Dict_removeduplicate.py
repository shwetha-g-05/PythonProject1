my_dict= {"a":1,"b":2,"c":1, "d":3}

unique = set()

result ={}

for key,value in my_dict.items():
    if value not in unique:
        result[key] = value
        unique.add(value)

print(result)