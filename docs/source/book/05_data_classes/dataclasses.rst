Data classes
------------

Data classes во многом похожи на именованные кортежи,
но имеют более широкие возможности. Например, атрибуты класса
могут быть изменяемые. 
Еще одно преимущество - data classes уменьшают количество кода в базовых методах
типа __str__, __repr__.

Data classes это новый функционал, он входит в стандартную бибилиотеку  начиная с Python 3.7.
Для предыдущих версий надо ставить отдельный модуль dataclasses или использовать сторонний
типа модуля attr.


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


.. code:: python

    In [11]: @dataclass(order=True, frozen=True)
        ...: class IPAddress:
        ...:     ip: str
        ...:     mask: int = 24
        ...:

    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip2 = IPAddress('10.2.2.2')

    In [14]: ip1 == ip2
    Out[14]: False

    In [15]: ip1 < ip2
    Out[15]: True

    In [16]: ip1.ip = 'aaa'
    ---------------------------------------------------------------------------
    FrozenInstanceError                       Traceback (most recent call last)
    <ipython-input-16-5a2e5685233c> in <module>
    ----> 1 ip1.ip = 'aaa'

    <string> in __setattr__(self, name, value)

    FrozenInstanceError: cannot assign to field 'ip'



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

