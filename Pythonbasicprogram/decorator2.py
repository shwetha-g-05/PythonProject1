def decorator(func):
    def wrapper():
        print("Before")
        result = func()
        print("After")
        return result

    return wrapper



@decorator
def add():
    return 5 +5

print(add())
