Примеры декораторов
-------------------

Декоратор отображает: имя функции и значение аргументов:

.. code:: python

    def debugger_with_args(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__} с args {args} и kwargs {kwargs}')
            return func(*args, **kwargs)
        return wrapper


    @debugger_with_args
    def func(a, b, verbose=True):
        return a, b, verbose


    In [3]: func(1, 'a', verbose=False)
    Вызываю функцию func с args (1, 'a') и kwargs {'verbose': False}
    Out[3]: (1, 'a', False)

Декоратор проверяет что все аргументы функции - строки:

.. code:: python

    def all_args_str(func):
        @wraps(func)
        def wrapper(*args):
            if not all(isinstance(arg, str) for arg in args):
                raise ValueError('Все аргументы должны быть строками')
            return func(*args)
        return wrapper


    @all_args_str
    def to_upper(*args):
        result = [s.upper() for s in args]
        return result


    In [6]: to_upper('a', 'b')
    Out[6]: ['A', 'B']

    In [7]: to_upper(1, 'b')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-7-bf0a0ae9f18c> in <module>
    ----> 1 to_upper(1, 'b')

    <ipython-input-4-9ddfa715e195> in wrapper(*args)
          3     def wrapper(*args):
          4         if not all(isinstance(arg, str) for arg in args):
    ----> 5             raise ValueError('Все аргументы должны быть строками')
          6         return func(*args)
          7     return wrapper

    ValueError: Все аргументы должны быть строками

