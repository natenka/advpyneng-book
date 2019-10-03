Декораторы без аргументов
-------------------------

Декоратор в Python это функция, которая используется для изменения
функции, метода или класса.
Декораторы используются для добавления какого-то функционала к функциям/классам.

Например, допустим, есть ряд функций к которым надо добавить print с информацией о том какая
функция вызывается:

.. code:: python

    def upper(string):
        return string.upper()

    def lower(string):
        return string.lower()

    def capitalize(string):
        return string.capitalize()

Самый базовый вариант будет вручную добавить строку в каждой функции:

.. code:: python

    def upper(string):
        print('Вызываю функцию upper')
        return string.upper()

    def lower(string):
        print('Вызываю функцию lower')
        return string.lower()

    def capitalize(string):
        print('Вызываю функцию capitalize')
        return string.capitalize()

Однако в этом случае будет очень много повторений, а главное,
при необходимости, например, заменить print на logging или просто изменить сообщение
придется редактировать большое количество функций.
Вместо этого можно создать одну функцию, которая перед вызовом исходной функции будет
выводить сообщение:

.. code:: python

    def verbose(func):
        def wrapper(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return wrapper

Функция verbose принимает как аргумент функцию, а затем возвращает
внутреннюю функцю wrapper внутри которой выводится сообщение, а затем
вызывается исходная функция. Для того чтобы функция verbose работала
надо заменить функцию upper внутренней функцией wrapper таким образом:

.. code:: python

    In [10]: upper = verbose(upper)

Теперь при вызове функции upper, вызывается внутренняя функция wrapper
и перед вызовом самой upper выводится сообщение:

.. code:: python

    In [12]: upper(s)
    Вызываю функцию upper
    Out[12]: 'LINE'

К сожалению, в этом случае надо после определения каждой функции
добавлять строку для модификации ее поведения:

.. code:: python

    def verbose(func):
        def wrapper(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return wrapper

    def upper(string):
        return string.upper()
    upper = verbose(upper)

    def lower(string):
        return string.lower()
    lower = verbose(lower)

    def capitalize(string):
        return string.capitalize()
    capitalize = verbose(capitalize)

Так как показанный выше синтаксис не очень удобен, в Python есть
другой синтаксис, который позволяет сделать то же самое более компактно:

.. code:: python

    def verbose(func):
        def wrapper(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return wrapper

    @verbose
    def upper(string):
        return string.upper()

    @verbose
    def lower(string):
        return string.lower()

    @verbose
    def capitalize(string):
        return string.capitalize()


При использовании декораторов, информация исходной функции
заменяется внутренней функцией декоратора:

.. code:: python

    In [2]: lower
    Out[2]: <function __main__.verbose.<locals>.wrapper(*args, **kwargs)>

    In [4]: lower?
    Signature: lower(*args, **kwargs)
    Docstring: <no docstring>
    File:      ~/repos/experiments/netdev_try/<ipython-input-1-32089045b87b>
    Type:      function

Чтобы исправить это необходимо воспользоваться декоратором wraps
из модуля functools:

.. code:: python

    In [5]: from functools import wraps

    In [6]: def verbose(func):
       ...:     @wraps(func)
       ...:     def wrapper(*args, **kwargs):
       ...:         print(f'Вызываю функцию {func.__name__}')
       ...:         return func(*args, **kwargs)
       ...:     return wrapper
       ...:
       ...: @verbose
       ...: def upper(string):
       ...:     return string.upper()
       ...:
       ...: @verbose
       ...: def lower(string):
       ...:     return string.lower()
       ...:
       ...: @verbose
       ...: def capitalize(string):
       ...:     return string.capitalize()
       ...:

    In [7]: lower
    Out[7]: <function __main__.lower(string)>

    In [8]: lower?
    Signature: lower(string)
    Docstring: <no docstring>
    File:      ~/repos/experiments/netdev_try/<ipython-input-6-13e6266ce16f>
    Type:      function

Декоратор wraps переносит информацию исходной функции на внутреннюю
и хотя это можно сделать и вручную, лучше пользоваться wraps.

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
    Out[30]: 9

    In [31]: @equals
        ...: @lines
        ...: @stars
        ...: def func(a, b):
        ...:     return a + b
        ...:

    In [32]: func(4,5)
    ==============================
    ------------------------------
    ******************************
    Out[32]: 9

    In [33]: def func(a, b):
        ...:     return a + b
        ...: func = equals(lines(stars(func)))

    In [34]: func(4,5)
    ==============================
    ------------------------------
    ******************************
    Out[34]: 9

Для некоторых декораторов порядок важен и тогда он будет
указан в документации. Например, декоратор abstractmethod 
должен `стоять первым над методом (быть самым внутренним) <https://docs.python.org/3/library/abc.html#abc.abstractmethod>`__:

.. code:: python

    class C(ABC):
        @abstractmethod
        def my_abstract_method(self, ...):
            ...
        @classmethod
        @abstractmethod
        def my_abstract_classmethod(cls, ...):
            ...
        @staticmethod
        @abstractmethod
        def my_abstract_staticmethod(...):
            ...

        @property
        @abstractmethod
        def my_abstract_property(self):
            ...
        @my_abstract_property.setter
        @abstractmethod
        def my_abstract_property(self, val):
            ...

