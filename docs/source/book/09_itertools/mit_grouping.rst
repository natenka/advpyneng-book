Группировка
-----------

chunked
~~~~~~~

Разбивает итерируемый объект на списки указанной длины:

.. code:: python

    more_itertools.chunked(iterable, n)

Пример:

.. code:: python

    In [6]: list(more_itertools.chunked(data, 2))
    Out[6]: [[1, 2], [3, 4], [5, 6], [7]]

    In [7]: list(more_itertools.chunked(data, 3))
    Out[7]: [[1, 2, 3], [4, 5, 6], [7]]

divide
~~~~~~

Разбивает итерируемый объект на n частей:

.. code:: python

    more_itertools.divide(n, iterable)

Пример:

.. code:: python

    In [25]: data
    Out[25]: [1, 2, 3, 4, 5, 6, 7]

    In [26]: g1, g2, g3 = more_itertools.divide(3, data)

    In [27]: list(g1)
    Out[27]: [1, 2, 3]

    In [28]: list(g2)
    Out[28]: [4, 5]

    In [29]: list(g3)
    Out[29]: [6, 7]

split_at
~~~~~~~~

Генерирует списки элементов из итерируемого объекта, где каждый список разделен
тем значением, для которого pred возвращает True (разедлитель не включен). 

.. code:: python

    more_itertools.split_at(iterable, pred)

Пример:

.. code:: python

    import time

    def file_gen(filename):
        with open(filename) as f:
            for idx, line in enumerate(f):
                print(idx)
                yield line

    f = file_gen('sh_cdp_neighbors_detail.txt')
    for items in more_itertools.split_at(f, lambda x: '------' in x):
        print(items)
        time.sleep(2)


unzip
~~~~~

Выполняет операцию противоположную zip:

.. code:: python

    more_itertools.unzip(iterable)

Пример:

.. code:: python

    In [2]: data = [('status', '*'),
       ...:         ('network', '1.23.78.0'),
       ...:         ('netmask', '24'),
       ...:         ('nexthop', '200.219.145.45'),
       ...:         ('metric', 'NA'),
       ...:         ('locprf', 'NA'),
       ...:         ('weight', '0'),
       ...:         ('path', '28135 18881 3549 6453 4755 45528'),
       ...:         ('origin', 'i')]

    In [3]: headers, values = more_itertools.unzip(data)

    In [4]: list(headers)
    Out[4]:
    ['status',
     'network',
     'netmask',
     'nexthop',
     'metric',
     'locprf',
     'weight',
     'path',
     'origin']

    In [5]: list(values)
    Out[5]:
    ['*',
     '1.23.78.0',
     '24',
     '200.219.145.45',
     'NA',
     'NA',
     '0',
     '28135 18881 3549 6453 4755 45528',
     'i']

grouper
~~~~~~~

.. code:: python

    more_itertools.grouper(iterable, n, fillvalue=None)

Пример:

.. code:: python

    In [6]: data = [1, 2, 3, 4, 5, 6, 7]

    In [8]: list(more_itertools.grouper(data, 3, 0))
    Out[8]: [(1, 2, 3), (4, 5, 6), (7, 0, 0)]

partition
~~~~~~~~~

.. code:: python

    more_itertools.partition(pred, iterable)


Пример:

.. code:: python

    In [10]: data = [1, 2, 'a', 'b', 5, 'c', 7]

    In [15]: is_false, is_true = more_itertools.partition(lambda x: str(x).isdigit(), data)

    In [16]: list(is_false)
    Out[16]: ['a', 'b', 'c']

    In [17]: list(is_true)
    Out[17]: [1, 2, 5, 7]
