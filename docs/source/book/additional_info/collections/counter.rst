Counter
--------------------

Counter - подкласс словаря для подсчета хешируемых объектов

.. code:: python

    class collections.Counter([iterable-or-mapping])


* ``elements()``
* ``most_common([n])``
* ``subtract([iterable-or-mapping])``
* ``total()`` (New in version 3.10)
* ``fromkeys(iterable)``


.. code:: python

    In [2]: c1 = Counter("aaabbbccccddddd")

    In [3]: c1
    Out[3]: Counter({'a': 3, 'b': 3, 'c': 4, 'd': 5})

    In [4]: list(c1.elements())
    Out[4]: ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']

    In [5]: c1.most_common(2)
    Out[5]: [('d', 5), ('c', 4)]

Операции с Counter

.. code:: python

    In [3]: c1
    Out[3]: Counter({'a': 3, 'b': 3, 'c': 4, 'd': 5})

    In [6]: c2 = Counter(a=1, d=5)

    In [7]: c2
    Out[7]: Counter({'a': 1, 'd': 5})

    In [9]: c1 - c2
    Out[9]: Counter({'a': 2, 'b': 3, 'c': 4})

    In [11]: c1.subtract(c2)

    In [12]: c1 + c2
    Out[12]: Counter({'a': 3, 'b': 3, 'c': 4, 'd': 5})


Пример использования
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import re
    import string
    from pprint import pprint
    from collections import Counter


    with open("text.txt") as f:
        content = f.read()

    clear_text = re.sub(f"[{string.punctuation}»«]", " ", content.lower())
    words = re.split("\s+", clear_text)
    stats = Counter(words)

    pprint(stats.most_common(20))

Результат

.. code:: python

    [('с', 9),
     ('не', 8),
     ('потоков', 6),
     ('в', 6),
     ('из', 5),
     ('это', 5),
     ('print', 5),
     ('при', 4),
     ('потоками', 4),
     ('если', 4),
     ('будет', 4),
     ('на', 4),
     ('работает', 4),
     ('работать', 3),
     ('и', 3),
     ('например', 3),
     ('нормально', 3),
     ('что', 3),
     ('сообщения', 3),
     ('может', 3)]

