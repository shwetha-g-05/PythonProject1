d = {"a":1, "b":2}

swapped = {}

for key in d:
    swapped[d[key]] = key

print(swapped)