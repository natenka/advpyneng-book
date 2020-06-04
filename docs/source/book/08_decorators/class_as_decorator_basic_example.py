class verbose:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Вызываю {self.func.__name__}')
        return self.func(*args, **kwargs)


@verbose
def upper(string):
    return string.upper()


In [121]: upper('a')
Вызываю upper
Out[121]: 'A'

In [122]: upper
Out[122]: <__main__.verbose at 0xb3fd390c>

