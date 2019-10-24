tee
~~~

Функция tee создает несколько независимых итераторов на основе исходных данных:

.. code:: python

    itertools.tee(iterable, n=2)

Пример использования:

.. code:: python

    In [30]: data = [1,2,3,4,5,6]

    In [31]: data_iter = iter(data)

    In [32]: duplicate_1, duplicate_2 = tee(data_iter)

    In [33]: list(duplicate_1)
    Out[33]: [1, 2, 3, 4, 5, 6]

    In [34]: list(duplicate_2)
    Out[34]: [1, 2, 3, 4, 5, 6]

Важная особенность tee - исходный итератор лучше не использовать,
иначе полученные итераторы начнут перебор не с начала:

.. code:: python

    In [35]: data_iter = iter(data)

    In [36]: duplicate_1, duplicate_2 = tee(data_iter)

    In [37]: next(data_iter)
    Out[37]: 1

    In [38]: next(data_iter)
    Out[38]: 2

    In [39]: list(duplicate_1)
    Out[39]: [3, 4, 5, 6]

    In [40]: list(duplicate_2)
    Out[40]: [3, 4, 5, 6]

При этом перебор одной копии, не влияет на вторую:

.. code:: python

    In [41]: data_iter = iter(data)

    In [42]: duplicate_1, duplicate_2 = tee(data_iter)

    In [43]: next(duplicate_1)
    Out[43]: 1

    In [44]: next(duplicate_1)
    Out[44]: 2

    In [45]: list(duplicate_1)
    Out[45]: [3, 4, 5, 6]

    In [46]: list(duplicate_2)
    Out[46]: [1, 2, 3, 4, 5, 6]

