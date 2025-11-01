#Log function
def log_function_call(function):
    def wrapper_function():
        print(f"Function {function.__name__} was called")
        function()
    return wrapper_function

@log_function_call
def say_hi():
    print("Hi there!")

say_hi()

#Timer Decorator
import time

current_time = time.time()
print(current_time)
def timer(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"Function {function.__name__} ran in {end_time-start_time} seconds")
    return wrapper_function

@timer
def fast_function():
    for i in range(1_000_000):
        i * i

@timer
def slow_function():
    for i in range(10_000_000):
        i * i

fast_function()
slow_function()

#Function call 3 times

def repeat(n):
    def decorator(function):
        def wrapper_function():
            for _ in range(n):
                function()
        return wrapper_function
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
