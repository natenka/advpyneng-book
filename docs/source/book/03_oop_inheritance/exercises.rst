Mixin task
----------

Создать класс Mixin, который будет автоматически добавлять к объекту методы:

* __ge__ - операция ``>=``
* __ne__ - операция ``!=``
* __le__ - операция ``<=``
* __gt__ - операция ``>``


Mixin предполагает, что в классе уже определены методы:

* ``__eq__`` - операция ``==``
* ``__lt__`` - операция ``<``


Mixin не должен использовать атрибуты класса IPAddress. Для работы методов
должны использоваться только существующие методы ``__eq__`` и ``__lt__``.

Пример класса IPAddress на котором можно проверить добавление методов:

.. code:: python

    import ipaddress


    class IPAddress:
        def __init__(self, ip):
            self._ip = int(ipaddress.ip_address(ip))

        def __str__(self):
            return f"IPAddress: {self._ip}"

        def __repr__(self):
            return f"IPAddress('{self._ip}')"

        def __eq__(self, other):
            return self._ip == other._ip

        def __lt__(self, other):
            return self._ip < other._ip
