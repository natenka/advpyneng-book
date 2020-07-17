Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

В стандартной библиотеке Python есть несколько готовых абстрактных классов, которые
можно использовать для наследования или проверки типа объекта.
Большая часть классов находится в ``collections.abc`` и часть из них показана в таблице ниже.

Полный перечень классов ``collections.abc`` доступен в `документации <https://docs.python.org/3/library/collections.abc.html>`__

.. tabularcolumns:: |l|L|L|L|

=================== ====================== ======================= ====================================================
ABC                 Наследует              Абстрактные методы      Mixin методы
=================== ====================== ======================= ====================================================
Container                                  __contains__  
Hashable                                   __hash__  
Iterable                                   __iter__  
Iterator            Iterable               __next__                __iter__  
Reversible          Iterable               __reversed__  
Generator           Iterator               send, throw             close, __iter__, __next__  
Sized                                      __len__  
Callable                                   __call__  
Collection          Sized,                 __contains__,
                    Iterable,              __iter__,
                    Container              __len__  
Sequence            Reversible,            __getitem__,            __contains__, __iter__, __reversed__,
                    Collection             __len__                 index, count
=================== ====================== ======================= ====================================================

Один из вариантов использования абстрактных классов collections.abc - это
проверка того поддерживает ли объект протокол.
Например, проверить является ли объект итерируемым можно таким образом:

.. code:: python

    In [1]: from collections.abc import Iterable

    In [2]: l1 = [1, 2, 3]

    In [3]: s1 = 'line'

    In [4]: n1 = 5

    In [5]: isinstance(l1, Iterable)
    Out[5]: True

    In [6]: isinstance(s1, Iterable)
    Out[6]: True

    In [7]: isinstance(n1, Iterable)
    Out[7]: False


 
Второй вариант использования классов collections.abc - наследование классов 
для поддержки определенного интерфейса. Например,
повторим пример с классом Network из `подраздела "Протокол последовательности" <https://pyneng2.readthedocs.io/en/latest/book/02_oop_special_methods/sequence_protocol.html>`__,
но теперь с наследованием класса Sequence:

.. code:: python

    In [1]: from collections.abc import Sequence
    In [2]: import ipaddress

    In [3]: class Network(Sequence):
       ...:     def __init__(self, network):
       ...:         self.network = network
       ...:         subnet = ipaddress.ip_network(self.network)
       ...:         self.addresses = [str(ip) for ip in subnet.hosts()]
       ...:

Пробуем создать экземпляр класса Network:

.. code:: python

    In [4]: net1 = Network('10.1.1.192/29')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-4-9c2ed79a8719> in <module>
    ----> 1 net1 = Network('10.1.1.192/29')

    TypeError: Cant instantiate abstract class Network with abstract methods __getitem__, __len__

Исключение указывает, что экземпляр не может быть создан, так как в классе Network
нет методов __getitem__ и __len__. Это методы, которые созданы как абстрактные и 
в таблице выше указаны в соответствующем столбце.
Добавляем эти методы в класс Network:

.. code:: python

    In [5]: class Network(Sequence):
       ...:     def __init__(self, network):
       ...:         self.network = network
       ...:         subnet = ipaddress.ip_network(self.network)
       ...:         self.addresses = [str(ip) for ip in subnet.hosts()]
       ...:
       ...:     def __getitem__(self, index):
       ...:         return self.addresses[index]
       ...:
       ...:     def __len__(self):
       ...:         return len(self.addresses)
       ...:

Теперь можно создать экземпляр класса Network и экземпляр поддерживает
обращение по индексу, а также работает функция len:

.. code:: python

    In [6]: net1 = Network('10.1.1.192/29')

    In [7]: net1.addresses
    Out[7]:
    ['10.1.1.193',
     '10.1.1.194',
     '10.1.1.195',
     '10.1.1.196',
     '10.1.1.197',
     '10.1.1.198']

    In [8]: len(net1)
    Out[8]: 6

    In [9]: net1[4]
    Out[9]: '10.1.1.197'

Кроме того, за счет наследования Sequence, в классе появились методы
__contains__, __iter__, __reversed__, index и count:

.. code:: python

    In [10]: '10.1.1.193' in net1
    Out[10]: True

    In [11]: i = iter(net1)

    In [12]: next(i)
    Out[12]: '10.1.1.193'

    In [13]: next(i)
    Out[13]: '10.1.1.194'


    In [14]: list(reversed(net1))
    Out[14]:
    ['10.1.1.198',
     '10.1.1.197',
     '10.1.1.196',
     '10.1.1.195',
     '10.1.1.194',
     '10.1.1.193']

    In [15]: net1.index('10.1.1.195')
    Out[15]: 2

    In [16]: net1.count('10.1.1.197')
    Out[16]: 1


