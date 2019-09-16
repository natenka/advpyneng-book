Декоратор classmethod
---------------------

Иногда нужно реализовать несколько способов создания экземпяра,
при этом в Python можно создавать только один метод __init__.
Конечно, можно реализовать все варианты в одном __init__,
но при этом часто параметры __init__ становятся или слишком общими,
или их слишком много.

Существует другой вариант решения проблемы - создать альтернативный
конструктор с помощью декоратора classmethod.

Пример альтернативного конструктора в стандартной библиотеке:

.. code:: python

    In [25]: r1 = {
        ...: 'hostname': 'R1',
        ...: 'OS': 'IOS',
        ...: 'Vendor': 'Cisco'
        ...: }

    In [28]: dict.fromkeys(['hostname', 'os', 'vendor'])
    Out[28]: {'hostname': None, 'os': None, 'vendor': None}

    In [29]: dict.fromkeys(['hostname', 'os', 'vendor'], '')
    Out[29]: {'hostname': '', 'os': '', 'vendor': ''}


.. code:: python

    import time
    from textfsm import clitable
    from base_ssh import BaseSSH

    class CiscoSSH(BaseSSH):
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            super().__init__(ip, username, password)
            self._ssh.send('enable\n')
            self._ssh.send(enable_password + '\n')
            if disable_paging:
                self._ssh.send('terminal length 0\n')
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)
            self._mgmt_ip = None

        @classmethod
        def default_params(cls, ip):
            params = {
                'ip': ip,
                'username': 'cisco',
                'password': 'cisco',
                'enable_password': 'cisco'}
            return cls(**params)


.. code:: python

    In [8]: r1 = CiscoSSH.default_params('192.168.100.1')

    In [9]: r1.send_show_command('sh clock')
    Out[9]: '*16:38:01.883 UTC Sun Jan 28 2018'
