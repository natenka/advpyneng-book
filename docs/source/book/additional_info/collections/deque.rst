collections.deque
-----------------

Deque поддерживает потокобезопасные, эффективные с точки зрения памяти
добавления и извлечения с обеих сторон двухсторонней очереди с примерно
одинаковой производительностью O(1) в любом направлении.

.. code:: python

    class collections.deque([iterable[, maxlen]])

Методы deque:

* ``append(x)``
* ``appendleft(x)``
* ``clear()``
* ``copy()``
* ``count(x)``
* ``extend(iterable)``
* ``extendleft(iterable)``
* ``index(x[, start[, stop]])``
* ``insert(i, x)``
* ``pop()``
* ``popleft()``
* ``remove(value)``
* ``reverse()``
* ``rotate(n=1)``
* ``maxlen``


append
~~~~~~

.. code:: python

    In [1]: from collections import deque

    In [2]: d = deque([1, 2, 3])

    In [3]: d.append(4)

    In [4]: d
    Out[4]: deque([1, 2, 3, 4])

    In [5]: d.appendleft(0)

    In [6]: d
    Out[6]: deque([0, 1, 2, 3, 4])


pop
~~~~

.. code:: python

    In [7]: d.pop()
    Out[7]: 4

    In [9]: d
    Out[9]: deque([0, 1, 2, 3])

    In [10]: d.popleft()
    Out[10]: 0

    In [11]: d
    Out[11]: deque([1, 2, 3])


index
~~~~~

.. code:: python

    In [12]: d[0]
    Out[12]: 1

    In [13]: d[-1]
    Out[13]: 3


rotate
~~~~~~

.. code:: python

    In [14]: d.rotate(1)

    In [15]: d
    Out[15]: deque([3, 1, 2])

    In [16]: d.rotate(-2)

    In [17]: d
    Out[17]: deque([2, 3, 1])


maxlen
~~~~~~

.. code:: python

    In [19]: d = deque([1, 2, 3, 4, 5], maxlen=5)

    In [20]: d
    Out[20]: deque([1, 2, 3, 4, 5])

    In [21]: d.append(6)

    In [22]: d
    Out[22]: deque([2, 3, 4, 5, 6])

    In [23]: d.appendleft(100)

    In [24]: d
    Out[24]: deque([100, 2, 3, 4, 5])

Пример использования
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    def tail(filename, n=10):
        'Return the last n lines of a file'
        with open(filename) as f:
            return deque(f, n)

