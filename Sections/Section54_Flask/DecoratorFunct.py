
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(5)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    # time.sleep(2)
    print("hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("Howdy!")


if __name__ == "__main__":
    say_hello()

    funct = delay_decorator(say_bye)
    funct()