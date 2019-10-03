def cool(func):
    func.cool = True
    return func



@cool
def sum_func(a, b):
    return a+b


def mul_func(a,b):
    return a*b


def identity(arg):
    return arg


@cool
def func2():
    pass


@cool
def func3():
    pass


'''
[f for k, f in select_cool_funcs.__dict__.items()
 if hasattr(f, 'cool') and f.cool]
Out[8]:
[<function select_cool_funcs.sum_func>,
 <function select_cool_funcs.func2>,
 <function select_cool_funcs.func3>]
'''
