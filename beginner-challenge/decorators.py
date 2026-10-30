def announce(func):
    print("Decorator is running")

    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result

    return wrapper

@announce
def multiply(a, b):
    print("Multiplying")
    return a * b

print("Program started")
answer = multiply(3, 4)
