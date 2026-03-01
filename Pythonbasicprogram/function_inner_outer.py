def outer():
    val = 30
    print(val)

    def inner():
        print("private value", val)

    def inner1():
        val = 29
        print("Inner1 value:", val)
    inner()
    inner1()
outer()