asynssh
=======

Модуль asynssh это реализация SSHv2 клиента и сервера. Модуль написан
с использованием asyncio и требует Python 3.6+.

Установка asyncssh (в книге показаны примеры на asyncssh 2.5.0):

::

    pip install asyncssh

Подключение выполняется таким образом:

.. code:: python

    In [1]: import asyncssh

    In [2]: ssh = await asyncssh.connect(
       ...:     "192.168.100.1",
       ...:     username="cisco",
       ...:     password="cisco",
       ...:     encryption_algs="+aes128-cbc,aes256-cbc",
       ...: )

Можно попробовать сначала подключиться без указания алгоритмов (без параметра
encryption_algs), а если возникнет ошибка, добавить недостающие алгоритмы.

После подключения, для работы с интерактивной сессией при подключении к сетевому
оборудовании, удобнее всего использовать метод open_session, так как он возвращает
три отдельных объекта stdin, stdout и stderr. В примере ниже stdin называется writer,
а stdout reader. Так как оборудование с Cisco IOS не выводит информацию на stderr,
далее этот объект не используется. Тут term_type равен Dumb, но при подключении к
Linux, например, тут может указываться, например, ``xterm-color``.

.. code:: python

    In [3]: writer, reader, stderr = await ssh.open_session(
       ...:     term_type="Dumb", term_size=(200, 24)
       ...: )

Дальше вся работа будет через объекты reader (класс SSHReader) и writer (класс SSHWriter)
и методы readuntil и write соответственно. При этом reader.readuntil это сопрограмма,
поэтому надо писать await, а writer.write не сопрограмма, поэтому await использовать не нужно:

.. code:: python

    In [4]: await reader.readuntil(">")
    Out[4]: '\r\nR1>'

    In [5]: writer.write("enable\n")

    In [6]: await reader.readuntil("Password")
    Out[6]: 'enable\r\nPassword'

    In [7]: writer.write("cisco\n")

    In [8]: await reader.readuntil("#")
    Out[8]: ': \r\nR1#'

Аналогично отправка команд и получение вывода:

.. code:: python

    In [9]: writer.write("terminal length 0\n")

    In [10]: await reader.readuntil("#")
    Out[10]: 'terminal length 0\r\nR1#'

    In [11]: writer.write("sh ip int br\n")

    In [12]: output = await reader.readuntil("#")

    In [13]: output
    Out[13]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                unassigned      YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nLoopback8                  10.8.8.8        YES manual up                    up      \r\nLoopback9                  10.90.90.1      YES manual up                    up      \r\nLoopback22                 10.2.2.2        YES NVRAM  up                    up      \r\nLoopback33                 unassigned      YES unset  up                    up      \r\nLoopback55                 5.5.5.5         YES NVRAM  up                    up      \r\nLoopback100                10.1.1.100      YES manual up                    up      \r\nLoopback123                123.1.2.3       YES NVRAM  up                    up      \r\nLoopback300                10.30.3.3       YES manual up                    up      \r\nR1#'

    In [14]: ssh.close()

Тот же код в виде функции:

.. code:: python

    from pprint import pprint
    import asyncio
    import asyncssh


    async def send_show(host, username, password, enable_password, command):
        ssh = await asyncssh.connect(
            host=host,
            username=username,
            password=password,
            encryption_algs="+aes128-cbc,aes256-cbc",
        )

        writer, reader, stderr = await ssh.open_session(
            term_type="Dumb", term_size=(200, 24)
        )
        output = await reader.readuntil(">")
        writer.write("enable\n")
        output = await reader.readuntil("Password")
        writer.write(f"{enable_password}\n")
        output = await reader.readuntil([">", "#"])
        writer.write("terminal length 0\n")
        output = await reader.readuntil("#")

        writer.write(f"{command}\n")
        output = await reader.readuntil("#")
        ssh.close()
        return output


    if __name__ == "__main__":
        r1 = {
            'host': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'enable_password': 'cisco',
        }
        result = asyncio.run(send_show(**r1, command="sh ip int br"))
        print(result)

Пока что это одна функция, которая последовательно выполняет ряд действий на
одном устройстве, но каждый await в функции, это точка где идет ожидание
ввода-вывода и в этих точках можно переключаться на другие функции.
Например, если запустить подключение с помощью этой функции на несколько устройств.

.. code:: python

    async def send_command_to_devices(devices, command):
        coroutines = [send_show(**device, command=command) for device in devices]
        result = await asyncio.gather(*coroutines)
        return result


    if __name__ == "__main__":
        devices = [
            {'host': '192.168.100.1',
             'username': 'cisco',
             'password': 'cisco',
             'enable_password': 'cisco'},
            {'host': '192.168.100.2',
             'username': 'cisco',
             'password': 'cisco',
             'enable_password': 'cisco'},
            {'host': '192.168.100.3',
             'username': 'cisco',
             'password': 'cisco',
             'enable_password': 'cisco'},
        ]
        result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
        pprint(result, width=120)

Теперь подключение выполняется на три устройства параллельно, с помощью gather.
