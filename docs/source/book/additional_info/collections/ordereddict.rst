collections.OrderedDict
-------------------------

OrderedDict похож на обычные словари, но имеют некоторые дополнительные возможности,
связанные с операциями упорядочивания. Начиная с Python 3.7, обычные словари
также стали упорядоченными, но при этом в OrderedDict остались несколько полезных возможностей:

* Обычный dict оптимизирован на операции mapping (getitem, setitem, deleteitem)
* OrderedDict оптимизирован под операции переупорядочивание
* Алгоритмически OrderedDict может обрабатывать частые операции переупорядочения лучше, чем dict
* При сравнении равенства словарей, OrderedDict учитывает соответствие порядка
* У OrderedDict есть метод ``move_to_end()`` для эффективного перемещения элемента в конец словаря

.. code:: python

    class collections.OrderedDict([items])


* ``popitem(last=True)``
* ``move_to_end(key, last=True)``

.. code:: python

    In [10]: d1 = {1: 100, 2: 200}

    In [11]: d2 = {2: 200, 1: 100}

    In [12]: d1 == d2
    Out[12]: True

    In [13]: from collections import OrderedDict

    In [14]: o1 = OrderedDict({1: 100, 2: 200})

    In [15]: o2 = OrderedDict({2: 200, 1: 100})

    In [16]: o1 == o2
    Out[16]: False


move_to_end
~~~~~~~~~~~~

.. code:: python

    In [17]: o1
    Out[17]: OrderedDict([(1, 100), (2, 200)])

    In [18]: o1.move_to_end(1)

    In [19]: o1
    Out[19]: OrderedDict([(2, 200), (1, 100)])
