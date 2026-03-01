def decorator(func):
    def wrapper():
        print("Good morning")
        func()
        print("Good evening")
    return wrapper


@decorator
def greet():
    print("Shwetha")

greet()









