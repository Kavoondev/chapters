import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        print("Do something before the function")
        function()
        #Do something after
        print("Do something after the function")
    return wrapper_function

@delay_decorator
def say_hello():
    print(("Hello!"))

decorated_function = delay_decorator(say_hello)
decorated_function()
