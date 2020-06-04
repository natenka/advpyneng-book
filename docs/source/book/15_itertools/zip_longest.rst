zip_longest
~~~~~~~~~~~

Функция zip_longest работает аналогично встроенной функции zip,
но не останавливается на самом коротком итерируемом объекте.

.. code:: python

    itertools.zip_longest(*iterables, fillvalue=None)

Пример использования:

.. code:: python

    In [20]: list(zip([1,2,3,4,5], [10,20]))
    Out[20]: [(1, 10), (2, 20)]

    In [21]: list(zip_longest([1,2,3,4,5], [10,20]))
    Out[21]: [(1, 10), (2, 20), (3, None), (4, None), (5, None)]

    In [22]: list(zip_longest([1,2,3,4,5], [10,20], fillvalue=0))
    Out[22]: [(1, 10), (2, 20), (3, 0), (4, 0), (5, 0)]

