chain
~~~~~

Функция chain ожидает несколько итерируемых объектов как аргумент и возвращает
единый итератор, который перебирает элементы каждого итерируемого объекта
так, как будто они составляют единый объект:

.. code:: python

    itertools.chain(*iterables)

Пример использования:

.. code:: python

    In [4]: line = 'test'

    In [5]: items = [1, 2, 3]

    In [6]: mapping = {'ios': '15.4', 'vendor': 'Cisco'}

    In [7]: for item in chain(line, items, mapping):
       ...:     print(item)
       ...:
    t
    e
    s
    t
    1
    2
    3
    ios
    vendor

