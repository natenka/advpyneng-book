Синтаксис
---------

Аннотация переменных
~~~~~~~~~~~~~~~~~~~~

.. note::

    Аннотацию не нужно будет писать абсолютно для всех переменных, так как
    многие типы будут автоматически вычисляться mypy.

Пример переменной:

.. code:: python

    username: str = 'user1'


Пример аннотации для разных встроенных типов данных:

.. code:: python

    length: int = 5
    summ: float = 5.5
    skip_line: bool = True
    line: str = "switchport mode access"

Списки, множества, словари:

.. code:: python

    from typing import List, Set, Dict, Tuple, Union

    vlans: List[int] = [10, 20, 100]
    unique_vlans: Set[int] = {1, 6, 10}

    book_price_map: Dict[str, float] = {'Good Omens': 22.0}

.. note::

    Начиная с Python 3.9 вместо List, Set, Dict, Tuple из модуля typing, можно будет
    использовать встроенные объекты list, set, dict, tuple.

Кортеж с фиксированным количеством элементов:

.. code:: python

    sw_info: Tuple[str, str, int] = ("sw1", "15.1(3)", 24)

Кортеж с произвольным количеством элементов:

.. code:: python

    vlans: Tuple[int, ...] = (1, 2, 3)

Список с элементами разного типа:

.. code:: python

    sw_info: List[Union[str, int]] = ("sw1", "15.1(3)", 24)


Также можно создавать аннотацию переменной без значения:

.. code:: python

    In [1]: username: str

    In [2]: username
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-2-407fefd38331> in <module>
    ----> 1 username

    NameError: name 'username' is not defined


Например, этот функционал используется в `Data classes <r2d2_add_link>`__ чтобы указать какие атрибуты
будут у экземпляров:

.. code:: python

    In [11]: @dataclass
        ...: class IPAddress:
        ...:     ip: str
        ...:     mask: int
        ...:

    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip1
    Out[13]: IPAddress(ip='10.1.1.1', mask=28)

Аннотация функции
~~~~~~~~~~~~~~~~~

Для параметров функции, аннотация пишется так же как для переменных, плюс добавляется
возвращаемое значение:

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


Аннотация классов
~~~~~~~~~~~~~~~~~

Аннотация методов пишется так же как аннотация функций.
Единственный нюанс методов - self пишется без аннотации.


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

Протоколы
~~~~~~~~~

Так как в Python достаточно часто будут встречаться функции с аргументами не конкретного типа,
а поддерживающие протокол, в typing есть объекты типа Iterable, Iterator и другие:

.. code:: python

    import ipaddress
    from typing import Iterable, Iterator, List

    def convert_int_to_str(integers: Iterable[int]) -> List[str]:
        return [str(x) for x in integers]

    class Network:
        def __init__(self, network: str) -> None:
            self.network = network
            subnet = ipaddress.ip_network(self.network)
            self.addresses = [str(ip) for ip in subnet.hosts()]

        def __iter__(self) -> Iterator:
            return iter(self.addresses)



Атрибут __annotations__
~~~~~~~~~~~~~~~~~~~~~~~

Атрибут __annotations__ содержит словарь с описанием аннотации.

Для глобальных переменных, он появляется как только есть аннотация хотя бы
в одной переменной:

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

Атрибут __annotations__ в функции:

.. code:: python

    def check_passwd(username: str, password: str,
                     min_length: int = 8, check_username: bool = True) -> bool:
        pass

    In [2]: check_passwd.__annotations__
    Out[2]:
    {'username': str,
     'password': str,
     'min_length': int,
     'check_username': bool,
     'return': bool}

В классе атрибут __annotations__ появляется в методах и в самом классе, если были созданы переменные класса:

.. code:: python

    class IPAddress:
            address_type: int = 4

            def __init__(self, ip: str, mask: int) -> None:
                self.ip = ip
                self.mask = mask

            def __repr__(self) -> str:
                return f"IPAddress({self.ip}/{self.mask})"



    In [9]: IPAddress.__annotations__
    Out[9]: {'address_type': int}

    In [10]: IPAddress.__repr__.__annotations__
    Out[10]: {'return': str}


