def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
        print("After calling")
    return wrapper

@log_function_call
def say_hello():
    print("Hello")

say_hello()