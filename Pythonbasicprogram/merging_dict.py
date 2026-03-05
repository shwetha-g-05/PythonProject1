d1 = {"a":1}
d2 = {"b":2}

print(d1 | d2)


d = {"a":3, "b":1, "c":2}

def get_value(item):
    return item[1]

soretd = dict(sorted(d.items(), key=get_value))
print(soretd)



