scrapli
=======

`scrapli <https://github.com/carlmontanari/scrapli>`__ поддерживает разные варианты
подключения: system, paramiko, ssh2, telnet, asyncssh, asynctelnet.
Тут рассматривается только asyncssh и asynctelnet.

.. note::

    Основы scrapli с использованием сихронного варианта транспорта рассматриваются
    в книге `Python для сетевых инженеров <https://pyneng.readthedocs.io/ru/latest/book/18_ssh_telnet/scrapli.html>`__.


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


.. code:: python

    import asyncio
    from scrapli.driver.core import AsyncIOSXEDriver


    async def send_show(device, command):
        async with AsyncIOSXEDriver(**device) as conn:
            result = await conn.send_command(command)
        return result.result


    r1 = {
       "host": "192.168.100.1",
       "auth_username": "cisco",
       "auth_password": "cisco",
       "auth_secondary": "cisco",
       "auth_strict_key": False,
       "transport": "asyncssh",
    }

    In [13]: asyncio.run(send_show(r1, "show clock"))
    Out[13]: '*08:55:10.229 UTC Wed Mar 31 2021'


.. code:: python

    async def send_command_to_devices(devices, command):
        coroutines = [send_show(device, command) for device in devices]
        result = await asyncio.gather(*coroutines)
        return result


    if __name__ == "__main__":
        common_params = {
            "auth_username": "cisco",
            "auth_password": "cisco",
            "auth_secondary": "cisco",
            "auth_strict_key": False,
            "transport": "asyncssh",
        }
        ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
        devices = [{"host": ip, **common_params} for ip in ip_list]
        result = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
        pprint(result, width=120)
