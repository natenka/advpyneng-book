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
        def inner(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return inner

Функция verbose принимает как аргумент функцию, а затем возвращает 
внутреннюю функцю inner внутри которой выводится сообщение, а затем
вызывается исходная функция. Для того чтобы функция verbose работала
надо заменить функцию upper внутренней функцией inner таким образом:

.. code:: python

    In [10]: upper = verbose(upper)

Теперь при вызове функции upper, вызывается внутренняя функция inner
и перед вызовом самой upper выводится сообщение:

.. code:: python

    In [12]: upper(s)
    Вызываю функцию upper
    Out[12]: 'LINE'

К сожалению, в этом случае надо после определения каждой функции 
добавлять строку для модификации ее поведения:

.. code:: python

    def verbose(func):
        def inner(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return inner

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
        def inner(*args, **kwargs):
            print(f'Вызываю функцию {func.__name__}')
            return func(*args, **kwargs)
        return inner

    @verbose
    def upper(string):
        return string.upper()

    @verbose
    def lower(string):
        return string.lower()

    @verbose
    def capitalize(string):
        return string.capitalize()




.. code:: python
.. code:: python
.. code:: python
.. code:: python

