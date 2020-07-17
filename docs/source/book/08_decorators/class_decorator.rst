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

