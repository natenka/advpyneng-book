Агрегирование значений
----------------------

first и last
~~~~~~~~~~~~

.. code:: python

    more_itertools.first(iterable[, default])
    more_itertools.last(iterable[, default])

.. code:: python

    In [42]: data = [1, 2, 'a', 'b', 5, 'c', 7]

    In [43]: more_itertools.first(data)
    Out[43]: 1

    In [44]: more_itertools.last(data)
    Out[44]: 7

all_equal
~~~~~~~~~

.. code:: python

    more_itertools.all_equal(iterable)

.. code:: python

    In [46]: more_itertools.all_equal([1, 1, 1])
    Out[46]: True

    In [47]: more_itertools.all_equal([1, 2, 1])
    Out[47]: False

