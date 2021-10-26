Декораторы в стандартной библиотеке
-----------------------------------

* classmethod
* staticmethod
* property
* contextlib: contextmanager
* dataclassess: dataclass

functools:

* cache
* lru_cache
* total_ordering
* singledispatch
* wraps

property
~~~~~~~~

.. code:: python

    class IPAddress:
        def __init__(self, address, mask):
            self._address = address
            self._mask = int(mask)

        @property
        def mask(self):
            return self._mask


classmethod
~~~~~~~~~~~

.. code:: python

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

staticmethod
~~~~~~~~~~~~

.. code:: python

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

        @staticmethod
        def _parse_show(command, command_output,
                       index_file='index', templates='templates'):
            attributes = {'Command': command,
                          'Vendor': 'cisco_ios'}
            cli_table = clitable.CliTable(index_file, templates)
            cli_table.ParseCmd(command_output, attributes)
            return [dict(zip(cli_table.header, row)) for row in cli_table]

        def send_show_command(self, command, parse=True):
            command_output = super().send_show_command(command)
            if not parse:
                return command_output
            return self._parse_show(command, command_output)



contextlib.contextmanager
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from contextlib import contextmanager
    from time import time, sleep


    @contextmanager
    def timecode():
        start = time()
        yield
        execution_time = time() - start
        print(f"Время выполнения: {execution_time:.2f}")


    In [9]: with timecode():
       ...:     sleep(3)
       ...:
    Время выполнения: 3.00


dataclasses.dataclass
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    @dataclass
    class IPAddress:
        ip: str
        mask: int


    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip1
    Out[13]: IPAddress(ip='10.1.1.1', mask=28)



functools.cache
~~~~~~~~~~~~~~~

.. code:: python

    from functools import cache, lru_cache


    @cache
    def factorial(n):
        print(f"{n=}")
        return n * factorial(n-1) if n else 1


    print(f"{factorial(4)=}")
    print(f"{factorial(5)=}")
    print(f"{factorial(6)=}")


без cache

::

    n=4
    n=3
    n=2
    n=1
    n=0
    factorial(4)=24
    n=5
    n=4
    n=3
    n=2
    n=1
    n=0
    factorial(5)=120
    n=6
    n=5
    n=4
    n=3
    n=2
    n=1
    n=0
    factorial(6)=720


с cache:

::

    n=4
    n=3
    n=2
    n=1
    n=0
    factorial(4)=24
    n=5
    factorial(5)=120
    n=6
    factorial(6)=720



functools lru_cache
~~~~~~~~~~~~~~~~~~~

.. code:: python

    from functools import lru_cache


    @lru_cache(maxsize=100)
    def fib(n):
        print(f"{n=}")
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)


    print([fib(n) for n in range(10)])
    print([fib(n) for n in range(16)])

::

    n=0
    n=1
    n=2
    n=3
    n=4
    n=5
    n=6
    n=7
    n=8
    n=9
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    n=10
    n=11
    n=12
    n=13
    n=14
    n=15
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]


.. code:: python

    @lru_cache(maxsize=1)
    def send_show_command(host, username, password, secret, device_type, show_command):
        with ConnectHandler(
            host=host,
            username=username,
            password=password,
            secret=secret,
            device_type=device_type,
        ) as ssh:
            ssh.enable()
            print(f"Вызываю команду {show_command}")
            result = ssh.send_command(show_command)
        return result

functools.singledispatch
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    @singledispatch
    def send_commands(command, device):
        print("singledispatch")
        raise NotImplementedError("Поддерживается только строка или iterable")


    @send_commands.register(str)
    def _(command, device):
        print("str")
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result


    @send_commands.register(Iterable)
    def _(config_commands, device):
        print("Аргумент iterable")
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_config_set(config_commands)
        return result

