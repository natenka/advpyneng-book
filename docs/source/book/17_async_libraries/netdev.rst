netdev
======

`netdev <https://github.com/selfuryon/netdev>`__ - это модуль, который позволяет
упростить использование asyncssh для сетевых устройств. Netdev использует
asyncssh, но при этом создает интерфейс и методы, которые нужны для работы
с сетевым оборудованием. Интерфейс работы похож на netmiko.


Установка netdev:

::

    pip install netdev

.. note::

    Текущая версия netdev 0.9.3 не поддерживает последние версии asyncssh.
    

Поддерживаемые платформы
~~~~~~~~~~~~~~~~~~~~~~~~

Поддерживаемые платформы:

* Cisco IOS
* Cisco IOS XE
* Cisco IOS XR
* Cisco ASA
* Cisco NX-OS
* HP Comware (like V1910 too)
* Fujitsu Blade Switches
* Mikrotik RouterOS
* Arista EOS
* Juniper JunOS
* Aruba AOS 6.X
* Aruba AOS 8.X
* Terminal

Параметры подключения
~~~~~~~~~~~~~~~~~~~~~

Основные параметры подключения:

* host - IP-адрес или имя хоста
* username - имя пользователя
* password - пароль
* secret (для Cisco IOS) - пароль на режим enable
* device_type - тип устройства

Процесс подключения немного отличается в зависимости от того используется
асинхронный менеджер контекста или нет. При подключении без менеджера контекста,
сначала надо передать параметры ``netdev.create``, а затем вызвать метод ``connect``:

.. code:: python

    In [1]: import netdev

    In [2]: r1 = {
       ...:     'device_type': 'cisco_ios',
       ...:     'host': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco',
       ...: }

    In [3]: ssh = netdev.create(**r1)

    In [4]: await ssh.connect()

После этого можно отправлять команды:

.. code:: python

    In [5]: ssh.base_prompt
    Out[5]: 'R1'

    In [6]: await ssh.check_enable_mode()
    Out[6]: True

    In [7]: await ssh.disconnect()

При использовании асинхронного менеджера контекста, open вызывать не надо:

.. code:: python

    In [9]: async with netdev.create(**r1) as ssh:
       ...:     print(await ssh.check_enable_mode())
    True

Отправка команд
~~~~~~~~~~~~~~~

В netdev есть два основных метода для отправки команд:

* ``send_command`` - отправить одну show команду
* ``send_config_set`` - отправить список команд в конфигурационном режиме (если
  команда одна, надо отправлять список с одной строкой)


Метод send_command
~~~~~~~~~~~~~~~~~~

Метод ``send_command`` позволяет отправить одну команду на устройство.

.. code:: python

    In [10]: await ssh.send_command("sh ip int br")
    Out[10]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                unassigned      YES NVRAM  up                    up      \nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \nLoopback11                 11.1.1.1        YES manual up                    up      \nLoopback99                 unassigned      YES unset  up                    up      \nLoopback100                10.1.1.100      YES manual up                    up      \nLoopback200                10.2.2.2        YES manual up                    up      \nTunnel0                    10.255.1.1      YES manual up                    down    \nTunnel1                    unassigned      YES unset  up                    down    \nTunnel9                    unassigned      YES unset  up                    down    '

Параметры команды:

.. code:: python

    ssh.send_command(
        command_string,
        pattern='',
        re_flags=0,
        strip_command=True,
        strip_prompt=True,
    )

Параметры strip_command и strip_prompt работают так же как в netmiko
и при значении False (по умолчанию True), добавляют в вывод команду и приглашение:

.. code:: python

    In [11]: await ssh.send_command("sh clock")
    Out[11]: '*05:54:20.671 UTC Thu Apr 8 2021'

    In [12]: await ssh.send_command("sh clock", strip_command=False, strip_prompt=False)
    Out[12]: 'sh clock\n*05:54:31.886 UTC Thu Apr 8 2021\nR1#'

Параметр pattern позволяет указывать какой строки ждать в выводе (нужно для
команд, которые запрашивают подтверждение или ввод информации):

.. code:: python

    In [13]: await ssh.send_command("copy run start", pattern="Destination filename")
    Out[13]: 'Destination filename [startup-config]? '

    In [14]: await ssh.send_command("\n")
    Out[14]: 'Building configuration...\n[OK]'



Метод send_config_set
~~~~~~~~~~~~~~~~~~~~~

Метод ``send_config_set`` позволяет отправить несколько команд конфигурационного
режима.

Пример использования:

.. code:: python

    In [16]: await ssh.send_config_set(["interface lo99", "ip address 10.99.9.9 255.25.255.255"])
    Out[16]: 'conf t\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#interface lo99\nR1(config-if)#ip address 10.99.9.9 255.25.255.255\nBad mask 0xFF19FFFF for address 10.99.9.9\nR1(config-if)#end\nR1#'

Для отправки одной команды, ее надо передать как список с одной строкой:

.. code:: python

    In [17]: await ssh.send_config_set(["interface lo99"])
    Out[17]: 'conf t\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#interface lo99\nR1(config-if)#end\nR1#'

Пример базового использования netdev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import asyncio
    import netdev


    async def send_show(device, command):
        async with netdev.create(**device) as ssh:
            result = await ssh.send_command(command)
            return result


    if __name__ == "__main__":
        r1 = {
            "device_type": "cisco_ios",
            "host": "192.168.100.1",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
        }
        output = asyncio.run(send_show(r1, "show ip int br"))
        print(output)


Подключение к нескольким устройствам
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from pprint import pprint
    import asyncio

    import netdev
    import yaml


    async def send_show(device, commands):
        result = {}
        if type(commands) == str:
            commands = [commands]
        try:
            async with netdev.create(**device) as ssh:
                for cmd in commands:
                    output = await ssh.send_command(cmd)
                    result[cmd] = output
                return result
        except netdev.exceptions.TimeoutError as error:
            print(error)
        except netdev.exceptions.DisconnectError as error:
            print(error)


    async def send_command_to_devices(devices, commands):
        coroutines = [send_show(device, commands) for device in devices]
        result = await asyncio.gather(*coroutines)
        return result


    if __name__ == "__main__":
        with open("devices_netdev.yaml") as f:
            devices = yaml.safe_load(f)
        result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
        pprint(result, width=120)

