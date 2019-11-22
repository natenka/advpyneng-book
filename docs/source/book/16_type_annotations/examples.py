Примеры использования аннотации типов
-------------------------------------

ignore-missing-imports
~~~~~~~~~~~~~~~~~~~~~~

::

    mypy --ignore-missing-imports example_04_class_basessh.py

Отложенное вычисление аннотаций типов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Работает в Python 3.7+ с импортом __future__

Использование имени класса в аннотации внутри этого же класса:

.. code:: python

    from __future__ import annotations
    import ipaddress


    class IPAddress:
        def __init__(self, ip: str) -> None:
            self.ip = ip

        def __add__(self, other: int) -> IPAddress:
            ip_int = int(ipaddress.ip_address(self.ip))
            sum_ip_str = str(ipaddress.ip_address(ip_int + other))
            return IPAddress(sum_ip_str)

Опциональный аргумент
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from typing import Union, List, Optional


    def check_passwd(username: str, password: str, min_length: int = 8,
                     check_username: bool = True,
                     forbidden_symbols: Union[List, None] = None) -> bool:
                     #forbidden_symbols: Optional[List] = None) -> bool:
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True

