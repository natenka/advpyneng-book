Декораторы с аргументами
------------------------

Иногда необходимо чтобы у декоратора была возможность принимать
аргументы. В таком случае надо добавить еще один уровень вложенности для декоратора.

Самый базовый вариант декоратора с аргументами, когда функция не подменяется
и аргументы функции не перехватываются. Тут к функции только добавляются атрибуты,
которые указаны при вызове декоратора:

.. code:: python

    def add_mark(**kwargs):
        def decorator(func):
            for key, value in kwargs.items():
                setattr(func, key, value)
            return func
        return decorator


    @add_mark(test=True, ordered=True)
    def test_function(a, b):
        return a + b


    In [73]: test_function.ordered
    Out[73]: True

    In [74]: test_function.test
    Out[74]: True

Пошагово происходит следующее: сначала вызывается функция add_mark
с соответствующими аргументами

.. code:: python

    decorate = add_mark(test=True, ordered=True)

Полученный результат будет декоратором, который ждет функцию как аргумент.
То есть, то же самое можно сделать в два шага:

.. code:: python

    def add_mark(**kwargs):
        def decorator(func):
            for key, value in kwargs.items():
                setattr(func, key, value)
            return func
        return decorator

    decorate = add_mark(test=True, ordered=True)

    @decorate
    def test_function(a, b):
        return a + b


    In [73]: test_function.ordered
    Out[73]: True

    In [74]: test_function.test
    Out[74]: True

Как только понадобится что-то делать с аргументами функции или добавить
что-то до или после вызова функции, добавляется еще один уровень.
Например, переделаем декоратор all_args_str таким образом, чтобы тип
данных можно было передавать как аргумент. Декоратор all_args_str:

.. code:: python

    def all_args_str(func):
        @wraps(func)
        def wrapper(*args):
            if not all(isinstance(arg, str) for arg in args):
                raise ValueError('Все аргументы должны быть строками')
            return func(*args)
        return wrapper

Добавляем еще один уровень для добавления аргумента:

.. code:: python

    def restrict_args_type(required_type):
        def decorator(func):
            @wraps(func)
            def wrapper(*args):
                if not all(isinstance(arg, required_type) for arg in args):
                    raise ValueError(f'Все аргументы должны быть {required_type.__name__}')
                return func(*args)
            return wrapper
        return decorator

Теперь, при применении декоратора, надо указывать какого типа должны быть аргументы:

.. code:: python

    In [89]: @restrict_args_type(str)
        ...: def to_upper(*args):
        ...:     result = [s.upper() for s in args]
        ...:     return result
        ...:

    In [90]: to_upper('a', 2)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-90-b46c3ca71e5d> in <module>
    ----> 1 to_upper('a', 2)

    <ipython-input-88-ea0c777e0f6e> in wrapper(*args)
          4             def wrapper(*args):
          5                 if not all(isinstance(arg, required_type) for arg in args):
    ----> 6                     raise ValueError(f'Все аргументы должны быть {required_type.__name__}')
          7                 return func(*args)
          8             return wrapper

    ValueError: Все аргументы должны быть str

    In [91]: to_upper('a', 'a')
    Out[91]: ['A', 'A']

    In [93]: @restrict_args_type(int)
        ...: def to_bin(*args):
        ...:     result = [bin(a) for a in args]
        ...:     return result
        ...:

    In [94]: to_bin(1,2,3)
    Out[94]: ['0b1', '0b10', '0b11']

    In [95]: to_bin('a', 'b')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-95-e4007cc06928> in <module>
    ----> 1 to_bin('a', 'b')

    <ipython-input-88-ea0c777e0f6e> in wrapper(*args)
          4             def wrapper(*args):
          5                 if not all(isinstance(arg, required_type) for arg in args):
    ----> 6                     raise ValueError(f'Все аргументы должны быть {required_type.__name__}')
          7                 return func(*args)
          8             return wrapper

    ValueError: Все аргументы должны быть int

Также при необходимости можно сделать готовые декораторы для определенных
типов данных:

.. code:: python

    In [96]: restrict_args_to_str = restrict_args_type(str)

    In [97]: restrict_args_to_int = restrict_args_type(int)

    In [98]: @restrict_args_to_str
        ...: def to_upper(*args):
        ...:     result = [s.upper() for s in args]
        ...:     return result
        ...:

    In [99]: @restrict_args_to_int
        ...: def to_bin(*args):
        ...:     result = [bin(a) for a in args]
        ...:     return result
        ...:

