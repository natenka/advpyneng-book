Data classes
------------

Data classes во многом похожи на именованные кортежи,
но имеют более широкие возможности. Например, атрибуты класса
могут быть изменяемые.

Часто в Python необходимо создавать классы в которых указаны только несколько переменных.
При этом, для реализации таких операций как сравнение экземпляров класса требуется создать
несколько специальных методов, добавить сюда строковое представление объекта
и для создания довольно простого класса, требуется много кода.


.. note::

    Data classes это новый функционал, он входит в стандартную бибилиотеку  начиная с Python 3.7.
    Для предыдущих версий надо ставить отдельный модуль dataclasses или использовать сторонний
    типа модуля attr.

Модуль dataclasses предоставляет декоратор dataclass с помощью которого
можно существенно упростить создание классов:

.. code:: python

    In [9]: dataclass?
    Signature:
    dataclass(
        _cls=None,
        *,
        init=True,
        repr=True,
        eq=True,
        order=False,
        unsafe_hash=False,
        frozen=False,
    )
    Docstring:
    Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If
    repr is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method function is added. If frozen is true, fields may
    not be assigned to after instance creation.
    File:      /usr/local/lib/python3.7/dataclasses.py
    Type:      function

Пример класса IPAddress:

.. code:: python

    class IPAddress:
        def __init__(self, ip, mask):
            self._ip = ip
            self._mask = mask

        def __repr__(self):
            return f"IPAddress({self.ip}/{self.mask})"

И соответствующего класса созданного с помощью dataclass:

.. code:: python

    In [11]: @dataclass
        ...: class IPAddress:
        ...:     ip: str
        ...:     mask: int
        ...:

    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip1
    Out[13]: IPAddress(ip='10.1.1.1', mask=28)

Для создания класса данных используется аннотация типов.
Декоратор dataclass использует указанные переменные и дополнительные настройки
для создания атрибутов для экземпляров класса, а также методов __init__, __repr__ и других.

Все переменные, которые определены на уровне класса, по умолчанию, будут прописаны
в методе __init__ и будут ожидаться как аргументы при создании экземпляра.

.. note::

    Типы указанные в определении класса не преобразуют атрибуты и не проверяют
    реальный тип данных аргументов.

Метод __post_init__
~~~~~~~~~~~~~~~~~~~

Метод __post_init__ позволяет добавлять дополнительную логику работы с переменными экземпляра.
Например, можно проверить тип данных или сделать дополнительные вычисления:

.. code:: python

    @dataclass
    class IPAddress:
        ip: str
        mask: int

        def __post_init__(self):
            if not isinstance(self.mask, int):
                self.mask = int(self.mask)


    In [46]: ip1 = IPAddress('10.10.1.1', '24')

    In [47]: ip1.mask
    Out[47]: 24



Параметры order и frozen
~~~~~~~~~~~~~~~~~~~~~~~~

При декорировании класса можно указать дополнительные параметры:

* frozen - контролирует можно ли менять значения переменных
* order - если равен True, добавляет к классу методы __lt__, __le__, __gt__, __ge__

Если параметр order равен True, экземпляры класса можно сравнивать и упорядочивать:

.. code:: python

    @dataclass(order=True)
    class IPAddress:
        ip: str
        mask: int


    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [14]: ip1 == ip2
    Out[14]: False

    In [15]: ip1 < ip2
    Out[15]: True


В данном случае, при сравнении и сортировке экземпляров класса возникает проблема
из-за лексикографической сортировки - экземпляры сортируются не так как хотелось бы:

.. code:: python

    In [24]: ip1 = IPAddress('10.10.1.1', 24)

    In [25]: ip2 = IPAddress('10.2.1.1', 24)

    In [26]: ip2 > ip1
    Out[26]: True

    In [27]: ip_list = [ip1, ip2]

    In [28]: ip_list
    Out[28]: [IPAddress(ip='10.10.1.1', mask=24), IPAddress(ip='10.2.1.1', mask=24)]

    In [30]: sorted(ip_list)
    Out[30]: [IPAddress(ip='10.10.1.1', mask=24), IPAddress(ip='10.2.1.1', mask=24)]

Функция field
~~~~~~~~~~~~~

Функция field позволяет указывать параметры работы с отдельными переменными.

.. code:: python

    dataclasses.field(*, default=MISSING, default_factory=MISSING,
                      repr=True, hash=None, init=True, compare=True, metadata=None)

Например, с помощью field можно указать, что какая-то переменная не должна отображаться
в __repr__:

.. code:: python

    @dataclass
    class User:
        username: str
        password: str = field(repr=False)


    In [49]: user1 = User('John', '12345')

    In [50]: user1
    Out[50]: User(username='John')


Все переменные, которые определены на уровне класса, по умолчанию, будут прописаны
в методе __init__ и будут ожидаться как аргументы при создании экземпляра.
Иногда в классе могут присутствовать переменные, которые вычисляются на основании
аргументов __init__, а не передаются как аргументы. В этом случае, можно
воспользоваться параметром init в field и вычислить значение динамически в__post_init__:

.. code:: python

    @dataclass
    class Book:
        title: str
        price: int
        quantity: int
        total: int = field(init=False)

        def __post_init__(self):
            self.total = self.price * self.quantity


    In [52]: book = Book('Good Omens', 35, 5)

    In [53]: book.total
    Out[53]: 175

    In [54]: book
    Out[54]: Book(title='Good Omens', price=35, quantity=5, total=175)


Функция field также поможет исправить ситуацию с сортировкой в классе IPAddress.
Указав ``compare=False`` при создании переменной, можно исключить ее из сравнения
и сортировки. Также в классе добавлена дополнительная переменная _ip,
которая содержит IP-адрес в виде числа. Для этой переменной ``init=False``, так как 
это значение не надо передавать при создании экземпляра, и ``repr=False``, так
как переменная не должна отображаться в строковом представлении:

.. code:: python

    @dataclass(order=True)
    class IPAddress:
        ip: str = field(compare=False)
        _ip: int = field(init=False, repr=False)
        mask: int

        def __post_init__(self):
            self._ip = int(ipaddress.ip_address(self.ip))


    In [40]: ip1 = IPAddress('10.10.1.1', 24)

    In [41]: ip2 = IPAddress('10.2.1.1', 24)

    In [42]: ip_list = [ip1, ip2]

    In [43]: sorted(ip_list)
    Out[43]: [IPAddress(ip='10.2.1.1', mask=24), IPAddress(ip='10.10.1.1', mask=24)]

    In [44]: ip1 > ip2
    Out[44]: True



Функции asdict, astuple, replace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    In [2]: from dataclasses import asdict, astuple, replace, dataclass

    In [3]: @dataclass(order=True, frozen=True)
       ...: class IPAddress:
       ...:     ip: str
       ...:     mask: int = 24
       ...:

    In [4]: ip1 = IPAddress('10.1.1.1', 28)

    In [5]: asdict(ip1)
    Out[5]: {'ip': '10.1.1.1', 'mask': 28}

    In [6]: astuple(ip1)
    Out[6]: ('10.1.1.1', 28)

    In [8]: replace(ip1, mask=24)
    Out[8]: IPAddress(ip='10.1.1.1', mask=24)

    In [9]: ip3 = replace(ip1, mask=24)

    In [10]: ip3
    Out[10]: IPAddress(ip='10.1.1.1', mask=24)

