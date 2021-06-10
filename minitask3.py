# should write:
# Call to deprecated function: some_old_function
# result of function is 3
#was caled:1 times
def deprecated(func):
    coun = 0
    def inner(*args):
        nonlocal coun
        coun +=1
        print(f'Call to deprecated function: {func.__name__}')
        res= func(*args)
        print(f'result of function is {res}')
        print(f'was caled:{coun} times')
    return inner

@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)
some_old_function(1,4)
