scrapli
=======

.. note::

    Основы scrapli с использованием синхронных вариантов транспорта рассматриваются
    в книге `Python для сетевых инженеров <https://pyneng.readthedocs.io/ru/latest/book/18_ssh_telnet/scrapli.html>`__.

`scrapli <https://github.com/carlmontanari/scrapli>`__ поддерживает разные варианты
подключения: system, paramiko, ssh2, telnet, asyncssh, asynctelnet.
Тут рассматривается только asyncssh и asynctelnet.

Доступные варианты асинхронного транспорта:

* asyncssh
* asynctelnet (реализация telnet на основе asyncio)

.. note::

    Рассматривается scrapli версии 2021.1.30.

    
Для синхронного транспорта, как и для синхронного, в scrapli есть два варианта
подключения: используя общий класс AsyncScrapli, который выбирает нужный driver
по параметру platform или конкретный driver, например, AsyncIOSXEDriver.
При этом параметры передаются те же самые и конкретному драйверу и Scrapli.

В целом методы и параметры методов такие же как и в синхронном варианте scrapli,
отличается транспорт, драйверы и то, что методы являются сопрограммами.

Параметры подключения
~~~~~~~~~~~~~~~~~~~~~

Основные параметры подключения:

* host - IP-адрес или имя хоста
* auth_username - имя пользователя
* auth_password - пароль
* auth_secondary - пароль на enable
* auth_strict_key - включить/отключить аутентификацию по ключам (по умолчанию включена)
* platform - нужно указывать при использовании AsyncScrapli
* transport - для async варианта transport указывать обязательно: asyncssh или asynctelnet
* transport_options - опции для конкретного транспорта

Процесс подключения немного отличается в зависимости от того используется
асинхронный менеджер контекста или нет. При подключении без менеджера контекста,
сначала надо передать параметры драйверу или AsyncScrapli, а затем вызвать метод open:

.. code:: python

    In [1]: from scrapli import AsyncScrapli

    In [2]: r1 = {
       ...:    "host": "192.168.100.1",
       ...:    "auth_username": "cisco",
       ...:    "auth_password": "cisco",
       ...:    "auth_secondary": "cisco",
       ...:    "auth_strict_key": False,
       ...:    "platform": "cisco_iosxe",
       ...:    "transport": "asyncssh",
       ...: }

    In [3]: ssh = AsyncScrapli(**r1)

    In [5]: await ssh.open()

После этого можно отправлять команды:

.. code:: python

    In [6]: await ssh.get_prompt()
    Out[6]: 'R1#'

    In [7]: await ssh.close()

При использовании асинхронного менеджера контекста, open вызывать не надо:

.. code:: python

    In [8]: async with AsyncScrapli(**r1) as ssh:
       ...:     print(await ssh.get_prompt())
    R1#


Использование драйвера
~~~~~~~~~~~~~~~~~~~~~~

Доступные async драйверы:

+--------------+-------------------+-------------------+
| Оборудование | Драйвер           | Параметр platform |
+==============+===================+===================+
| Cisco IOS-XE | AsyncIOSXEDriver  | cisco_iosxe       |
+--------------+-------------------+-------------------+
| Cisco NX-OS  | AsyncNXOSDriver   | cisco_nxos        |
+--------------+-------------------+-------------------+
| Cisco IOS-XR | AsyncIOSXRDriver  | cisco_iosxr       |
+--------------+-------------------+-------------------+
| Arista EOS   | AsyncEOSDriver    | arista_eos        |
+--------------+-------------------+-------------------+
| Juniper JunOS| AsyncJunosDriver  | juniper_junos     |
+--------------+-------------------+-------------------+

Пример подключения с использованием драйвера IOSXEDriver (технически
подключение выполняется к Cisco IOS):

.. code:: python

    In [10]: from scrapli.driver.core import AsyncIOSXEDriver

    In [11]: r1_driver = {
        ...:    "host": "192.168.100.1",
        ...:    "auth_username": "cisco",
        ...:    "auth_password": "cisco",
        ...:    "auth_secondary": "cisco",
        ...:    "auth_strict_key": False,
        ...:    "transport": "asyncssh",
        ...: }

    In [12]: async with AsyncIOSXEDriver(**r1_driver) as ssh:
        ...:     print(await ssh.get_prompt())
    R1#

Пример базового использования scrapli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В остальном, принципы работы те же, что и с синхронным вариантом.

Пример подключения к одному устройству с помощью asyncssh и AsyncScrapli:

.. code:: python

    import asyncio
    from scrapli import AsyncScrapli
    from scrapli.exceptions import ScrapliException

    r1 = {
        "host": "192.168.100.1",
        "auth_username": "cisco",
        "auth_password": "cisco",
        "auth_secondary": "cisco",
        "auth_strict_key": False,
        "timeout_socket": 5,  # timeout for establishing socket/initial connection in seconds
        "timeout_transport": 10,  # timeout for ssh|telnet transport in seconds
        "platform": "cisco_iosxe",
        "transport": "asyncssh",
    }


    async def send_show(device, command):
        try:
            async with AsyncScrapli(**device) as conn:
                result = await conn.send_command(command)
                return result.result
        except ScrapliException as error:
            print(error, device["host"])


    if __name__ == "__main__":
        output = asyncio.run(send_show(r1, "show ip int br"))
        print(output)

Подключение к нескольким устройствам
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Пример подключения к нескольким устройствам:

.. code:: python

    from pprint import pprint
    import asyncio

    import yaml
    from scrapli import AsyncScrapli
    from scrapli.exceptions import ScrapliException


    async def send_show(device, show_commands):
        cmd_dict = {}
        if type(show_commands) == str:
            show_commands = [show_commands]
        try:
            async with AsyncScrapli(**device) as ssh:
                for cmd in show_commands:
                    reply = await ssh.send_command(cmd)
                    cmd_dict[cmd] = reply.result
            return cmd_dict
        except ScrapliException as error:
            print(error, device["host"])


    async def send_command_to_devices(devices, commands):
        coroutines = [send_show(device, commands) for device in devices]
        result = await asyncio.gather(*coroutines)
        return result


    if __name__ == "__main__":
        with open("devices_async.yaml") as f:
            devices = yaml.safe_load(f)
        result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
        pprint(result, width=120)

Файл devices_async.yaml:

.. code:: yaml

    - host: 192.168.100.1
      auth_username: cisco
      auth_password: cisco
      auth_secondary: cisco
      auth_strict_key: false
      timeout_socket: 5
      timeout_transport: 10
      platform: cisco_iosxe
      transport: asyncssh
    - host: 192.168.100.2
      auth_username: cisco
      auth_password: cisco
      auth_secondary: cisco
      auth_strict_key: false
      timeout_socket: 5
      timeout_transport: 10
      platform: cisco_iosxe
      transport: asyncssh
    - host: 192.168.100.3
      auth_username: cisco
      auth_password: cisco
      auth_secondary: cisco
      auth_strict_key: false
      timeout_socket: 5
      timeout_transport: 10
      platform: cisco_iosxe
      transport: asyncssh


Подключение с транспортом asynctelnet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При подключении asynctelnet надо указать транспорт asynctelnet и
порт 23. Кроме того, надо данный момент (scrapli 2021.1.30) при подключении
asynctelnet к недоступному адресу таймаут будет через 2 минуты, чтобы
уменьшить его, можно использовать async_timeout:

.. code:: python

    import asyncio
    from scrapli.driver.core import AsyncIOSXEDriver
    from scrapli.exceptions import ScrapliException
    from async_timeout import timeout

    r1 = {
        "host": "192.168.100.11",
        "auth_username": "cisco",
        "auth_password": "cisco",
        "auth_secondary": "cisco",
        "auth_strict_key": False,
        "transport": "asynctelnet",
        "port": 23,
    }


    async def send_show(device, command):
        # На данный момент (scrapli 2021.1.30) таймаут при подключении к недоступному
        # хосту будет 2 минуты, поэтому пока что лучше добавлять wait_for или
        # async_timeout вокруг подключения
        try:
            async with timeout(10):
                async with AsyncIOSXEDriver(**device) as ssh:
                    result = await ssh.send_command(command)
                    return result.result
        except ScrapliException as error:
            print(error, device["host"])
        except asyncio.exceptions.TimeoutError:
            print("asyncio.exceptions.TimeoutError", device["host"])


    if __name__ == "__main__":
        output = asyncio.run(send_show(r1, "show ip int br"))
        print(output)

