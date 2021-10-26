Стек декораторов
----------------

К функции может применяться несколько декораторов. Порядок применения
декораторов будет зависеть от того в каком порядке они записаны:

.. code:: python

    def stars(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('*'*30)
            return func(*args, **kwargs)
        return wrapper


    def lines(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('-'*30)
            return func(*args, **kwargs)
        return wrapper


    def equals(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('='*30)
            return func(*args, **kwargs)
        return wrapper


    @stars
    @lines
    @equals
    def func(a, b):
        return a + b


    In [23]: func(4,5)
    ******************************
    ------------------------------
    ==============================
    Out[23]: 9

    In [24]: def func(a, b):
        ...:     return a + b
        ...: func = stars(lines(equals(func)))

    In [30]: func(4,5)
    ******************************
    ------------------------------
    ==============================

