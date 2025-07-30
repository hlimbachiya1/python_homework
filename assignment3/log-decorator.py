# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        pos = list(args) if args else "none"
        kw = dict(kwargs) if kwargs else "none"
        

# To write a log record:
        logger.log(logging.INFO,
                   f"function: {func.__name__} positional parameters: {pos} keyword parameters: {kw} return: {result}")
        return result
    return wrapper

#function1 =  no parameter and return nothing
@logger_decorator
def say_hello():
    print("Hello World!")
    return None

#function2: variable positional argument. return trures
@logger_decorator
def var_positional(*args):
    return True

# Function3: Variable keyword arguments, returns logger_decorator
@logger_decorator
def var_keyword(**kwargs):
    return logger_decorator

if __name__=="__main__":
    print("=== Testing Logger Decorator ===")
    say_hello()
    var_positional(1,2,3)
    var_keyword(a=10, b=20)
    print("Check decorator.log file for logged information.")