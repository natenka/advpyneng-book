Основы
------

Аннотация типов - это дополнительное описание в классах, функциях, переменных,
которое указывает какой тип данных должен быть в этом месте.
Это новый функционал, который был добавлен в последних версиях Python (Python 3.6+).

При этом указанные типы не проверяются и не форсируются самим Python. Для проверки
типов данных надо использовать отдельные модули, например, mypy.

Аннотация функции
~~~~~~~~~~~~~~~~~

Пример аннотации функции:

.. code:: python

    import ipaddress


    def check_ip(ip: str) -> bool:
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError as err:
            return False

Пример аннотации функции со значениями по умолчанию:

.. code:: python

    def check_passwd(username: str, password: str,
                     min_length: int = 8, check_username: bool = True) -> bool:
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True

Атрибут __annotations__:

.. code:: python

    In [2]: check_passwd.__annotations__
    Out[2]:
    {'username': str,
     'password': str,
     'min_length': int,
     'check_username': bool,
     'return': bool}

Аннотация переменных
~~~~~~~~~~~~~~~~~~~~

Пример переменной:

.. code:: python

    username: str = 'user1'

Также можно создавать аннотацию переменной без значения:

.. code:: python

    In [1]: username: str

    In [2]: username
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-2-407fefd38331> in <module>
    ----> 1 username

    NameError: name 'username' is not defined

    In [3]: __annotations__
    Out[3]: {'username': str}

Например, этот функционал используется в Data classes:

.. code:: python

    In [11]: @dataclass
        ...: class IPAddress:
        ...:     ip: str
        ...:     mask: int
        ...:

    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip1
    Out[13]: IPAddress(ip='10.1.1.1', mask=28)


Писать аннотацию для переменных нужно далеко не всегда. Как правило, того типа который
"угадал" mypy достаточно. Например, в этом случае mypy понимает, что ip это строка:

.. code:: python

    ip = '10.1.1.1'

И не будет выводить никаких ошибок:

::

    $ mypy example_03_variable.py

    Success: no issues found in 1 source file

Однако, если переменная может быть и строкой и числом:

.. code:: python

    ip = '10.1.1.1'
    ip = 3

mypy посчитает это ошибкой:

::

    example_03_variable.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")
    Found 1 error in 1 file (checked 1 source file)

В таком случае надо явно указать, что переменная может быть числом или строкой:

.. code:: python

    from typing import Union

    ip: Union[int, str] = '10.1.1.1'
    ip = 3


Аннотация классов
~~~~~~~~~~~~~~~~~

* не пишем аннотацию для self


.. code:: python

    class IPAddress:
        def __init__(self, ip: str, mask: int) -> None:
            self.ip = ip
            self.mask = mask

        def __repr__(self) -> str:
            return f"IPAddress({self.ip}/{self.mask})"


Аннотация типов и наследование
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Дочерний класс должен поддерживать те же типы данных, что и родительский:

.. code:: python

    import time
    from typing import Union, List


    class BaseSSH:
        def __init__(self, ip: str, username: str, password: str) -> None:
            self.ip = ip
            self.username = username
            self.password = password

        def send_config_commands(self, commands: Union[str, List[str]]) -> str:
            if isinstance(commands, str):
                commands = [commands]
            for command in commands:
                time.sleep(0.5)
            return 'result'


    class CiscoSSH(BaseSSH):
        def __init__(self, ip: str, username: str, password: str,
                     enable_password: str = None, disable_paging: bool = True) -> None:
            super().__init__(ip, username, password)

        def send_config_commands(self, commands: List[str]) -> str:
            return 'result'

В этом случае будет ошибка:

::
    $ mypy example_07_class_inheritance.py
    example_07_class_inheritance.py:25: error: Argument 1 of "send_config_commands" is incompatible with supertype "BaseSSH"; supertype defines the argument type as "Union[str, List[str]]"
    Found 1 error in 1 file (checked 1 source file)


