#create decorator log_and_count which will print out arguments of decorated function
#and update dictionary my_counter with items where key is name of function or 'basic function'
# if in decorator parametres key is given. Values will number, how many times was function called
my_counter = {}
def log_and_count(key='func'):
    global my_counter
    def count(func):
        # here I am setting values to 0 and if key is given prevent creating new item for function which is basic one
        if key == 'basic functions':
            my_counter['basic functions'] = 0
        else:
            my_counter[func.__name__] = 0
        def inner(*args,**kwargs):
            #Counting how many times functions were called
            if key=='basic functions':
                my_counter['basic functions'] += 1
            else:
                my_counter[func.__name__] += 1
            #print out parametres of functions    
            print('called', func.__name__, 'with: {} and {}'.format(args, kwargs))
            return func(*args,**kwargs)
        return inner
    return count


@log_and_count(key = 'basic functions')
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions')
def f2(a, b=3):
    return a ** 2 + b

@log_and_count()
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
print(my_counter)