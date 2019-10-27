Просмотр значений в итераторе, не теряя значений
------------------------------------------------

spy
~~~

.. code:: python

    more_itertools.spy(iterable, n=1)

Пример

.. code:: python

    In [19]: def file_gen(filename):
        ...:     with open(filename) as f:
        ...:         for idx, line in enumerate(f):
        ...:             print(idx)
        ...:             yield line
        ...:

    In [20]: f = file_gen('sh_cdp_neighbors_detail.txt')

    In [21]: f
    Out[21]: <generator object file_gen at 0xb28bd4ec>

    In [23]: first, f = more_itertools.spy(f)
    0

    In [24]: first
    Out[24]: ['SW1#show cdp neighbors detail\n']

    In [25]: f
    Out[25]: <itertools.chain at 0xb38c184c>

    In [26]: next(f)
    Out[26]: 'SW1#show cdp neighbors detail\n'

