collapse
--------

.. code:: python

    more_itertools.collapse(iterable, base_type=None, levels=None)

Пример

.. code:: python

    In [37]: iterable = [(1, 2), ([3, 4], [[5], [6]])]

    In [38]: list(more_itertools.collapse(iterable))
    Out[38]: [1, 2, 3, 4, 5, 6]

