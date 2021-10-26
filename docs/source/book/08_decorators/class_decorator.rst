Декоратор класса
----------------

.. code:: python


    CLASS_MAPPER_BASE = {}

    def register_class(cls):
        CLASS_MAPPER_BASE[cls.device_type] = cls.__name__
        return cls


    @register_class
    class CiscoSSH:
        device_type = 'cisco_ios'
        def __init__(self, ip, username, password):
            pass


    @register_class
    class JuniperSSH:
        device_type = 'juniper'
        def __init__(self, ip, username, password):
            pass


Декоратор добавляет метод pprint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from rich import print as rprint


    def add_pprint(cls):
        def pprint(self, methods=False):
            methods_class_attrs = vars(type(self))
            methods = {
                name: method
                for name, method in methods_class_attrs.items()
                if not name.startswith("__") and callable(method)
            }
            self_attrs = vars(self)
            rprint(self_attrs)
            if methods:
                rprint(methods)

        cls.pprint = pprint
        return cls


.. code:: python

    @add_pprint
    class IPv4Address:
        def __init__(self, ip):
            self.ip = ip
            self._int_ip = int(ip_address(ip))

        def as_int(self):
            return self._int_ip


    In [15]: ip1 = IPv4Address("10.1.1.1")

    In [16]: ip1.pprint()
    {'ip': '10.1.1.1', '_int_ip': 167837953}
    {
        'as_int': <function IPv4Address.as_int at 0xb4235df0>,
        'pprint': <function add_pprint.<locals>.pprint at 0xb4235388>
    }

    In [17]: ip1.pprint(methods=True)
    {'ip': '10.1.1.1', '_int_ip': 167837953}
    {
        'as_int': <function IPv4Address.as_int at 0xb4235df0>,
        'pprint': <function add_pprint.<locals>.pprint at 0xb4235388>
}
