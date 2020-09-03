
.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst

Задание 5.1
~~~~~~~~~~~

Создать класс Route с использованием dataclass. У экземпляров класса должны быть
доступны переменные: prefix, nexthop и protocol.
В строковом представлении экземпляров не должна выводиться информация о протоколе.

Пример создания экземпляра класса:

.. code:: python

    In [2]: route1 = Route('10.1.1.0/24', '10.2.2.2', 'OSPF')

После этого, должны быть доступны переменные prefix, nexthop и protocol:

.. code:: python

    In [3]: route1.nexthop
    Out[3]: '10.2.2.2'

    In [4]: route1.prefix
    Out[4]: '10.1.1.0/24'

    In [5]: route1.protocol
    Out[5]: 'OSPF'


Строковое представление:

.. code:: python

    In [6]: route1
    Out[6]: Route(prefix='10.1.1.0/24', nexthop='10.2.2.2')


Задание 5.2
~~~~~~~~~~~~

Дополнить класс IPAddress: добавить метод, который позволит
выполнять сложение экземпляра класса IPAddress и числа.
В результате сложения должен возвращаться новый экземпляр класса IPAddress.

Пример создания экземпляра класса:

.. code:: python

    In [7]: ip1 = IPAddress('10.10.1.1', 24)

Суммирование:

.. code:: python

    In [8]: ip1
    Out[8]: IPAddress(ip='10.10.1.1', mask=24)

    In [9]: ip1 + 5
    Out[9]: IPAddress(ip='10.10.1.6', mask=24)

    In [10]: ip2 = ip1 + 5

    In [11]: isinstance(ip2, IPAddress)
    Out[11]: True

Дполнить такой класс:

.. code:: python

    import ipaddress
    from dataclasses import dataclass, field


    @dataclass(order=True)
    class IPAddress:
        ip: str = field(compare=False)
        _ip: int = field(init=False, repr=False)
        mask: int

        def __post_init__(self):
            self._ip = int(ipaddress.ip_address(self.ip))

Задание 5.3
~~~~~~~~~~~~

Дополнить класс Book: добавить метод to_dict.
Метод to_dict должен возвращать словарь в котором:

* ключи - имена переменных экземпляра
* значения - значения переменных

В словаре должны быть все переменные, кроме тех, которые начинаются на _.

Пример создания экземпляра класса:

.. code:: python

    In [4]: b1 = Book('Good Omens', 35, 5)

В этом случае должен возвращаться такой словарь:

.. code:: python

    In [5]: b1.to_dict()
    Out[5]: {'title': 'Good Omens', 'price': 35.0, 'quantity': 124, 'total': 4340.0}

Обратите внимание, что в словаре не только простые переменные, но и переменные,
которые созданы через property.

.. code:: python

    from dataclasses import dataclass, field

    @dataclass
    class Book:
        title: str
        price: float
        _price: float = field(init=False, repr=False)
        quantity: int = 0

        @property
        def total(self):
            return round(self.price * self.quantity, 2)

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError('Значение должно быть числом')
            if not value >= 0:
                raise ValueError('Значение должно быть положительным')
            self._price = float(value)

Задание 5.4
~~~~~~~~~~~

Создать класс IPv4Network с использованием dataclass. У экземпляров класса должны быть
доступны:

* переменные: network, broadcast, hosts, allocated, unassigned
* метод allocate

Пример создания экземпляра класса:

.. code:: python

    In [3]: net1 = IPv4Network('10.1.1.0/29')

После этого, должна быть доступна переменная network:

.. code:: python

    In [6]: net1.network
    Out[6]: '10.1.1.0/29'


Broadcast адрес должен быть записан в атрибуте broadcast:

.. code:: python

    In [7]: net1.broadcast
    Out[7]: '10.1.1.7'

Также должен быть создан атрибут allocated в котором будет
храниться список с адресами, которые назначены на каком-то
устройстве/хосте. Изначально атрибут равен пустому списку:

.. code:: python

    In [8]: print(net1.allocated)
    []


Атрибут hosts должен возвращать список IP-адресов, которые входят в сеть,
не включая адрес сети и broadcast:

.. code:: python

    In [9]: net1.hosts
    Out[9]: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6']

Метод allocate ожидает как аргумент IP-адрес. Указанный адрес
должен быть записан в список в атрибуте net1.allocated и удален из списка unassigned:

.. code:: python

    In [10]: net1 = IPv4Network('10.1.1.0/29')

    In [11]: print(net1.allocated)
    []

    In [12]: net1.allocate('10.1.1.6')

    In [13]: net1.allocate('10.1.1.3')

    In [14]: print(net1.allocated)
    ['10.1.1.6', '10.1.1.3']


Атрибут unassigned возвращает возвращает список со свободными адресами:

.. code:: python

    In [15]: net1 = IPv4Network('10.1.1.0/29')

    In [16]: net1.allocate('10.1.1.4')
        ...: net1.allocate('10.1.1.6')
        ...: net1.allocate('10.1.1.8')
        ...:

    In [17]: net1.unassigned
    Out[17]: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.5']


