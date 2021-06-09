#create multiple call function:f()()()()-->'foooo'  ,  f()()('s') -->'foos'  ,  f('it')-->  'fit'
class dec:
    selid = set()
    def __init__(self,func):
        self.func=func
        print(self.func.__name__, end='')
    def __call__(self, ar=''):
        self.selid.add(id(self.__call__))
        if ar:
            self.func(ar='')
            print(ar)
        else:print('o',end='')
        return self.__call__
@dec
def f(ar=''):
    pass
  #  return func
f()()('x')




