islice
~~~~~~

Функция islice

.. code:: python

    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, step])

Пример использования:

.. code:: python

    In [59]: list(islice(range(100), 5))
    Out[59]: [0, 1, 2, 3, 4]

    In [60]: list(islice(range(100), 5, 10))
    Out[60]: [5, 6, 7, 8, 9]

    In [61]: list(islice(range(100), 5, 10, 2))
    Out[61]: [5, 7, 9]

    In [62]: list(islice(range(100), 5, 20, 2))
    Out[62]: [5, 7, 9, 11, 13, 15, 17, 19]

    In [63]: list(islice(range(100), 5, 20, 3))
    Out[63]: [5, 8, 11, 14, 17]

