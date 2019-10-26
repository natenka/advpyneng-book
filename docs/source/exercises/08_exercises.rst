
.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst

Задание 8.1
~~~~~~~~~~~

Создать генератор get_ip_from_cfg, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства и возвращает все IP-адреса,
которые настроены на интерфейсах.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например: ('10.0.1.1', '255.255.255.0')

Проверить работу генератора на примере файла config_r1.txt.

Задание 8.1a
~~~~~~~~~~~

Создать генератор get_intf_ip, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства и возвращает все интерфейсы и IP-адреса,
которые настроены на интерфейсах.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:

* первый элемент кортежа - имя интерфейса
* второй элемент кортежа - IP-адрес
* третий элемент кортежа - маска

Например: ``('FastEthernet', '10.0.1.1', '255.255.255.0')``

Проверить работу генератора на примере файла config_r1.txt.


Задание 8.1b
~~~~~~~~~~~

Создать генератор get_intf_ip_from_files, который ожидает как аргумент
произвольное количество файлов с конфигурацией устройств и возвращает интерсейсы и IP-адреса,
которые настроены на интерфейсах.

Генератор должен обрабатывать конфигурацию и возвращать словарь
для каждого файла на каждой итерации:

* ключ - hostname
* значение словарь, в котором:

  * ключ - имя интерфейса
  * значение - кортеж с IP-адресом и маской

Пример:

.. code:: python

    {'r1': {'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
            'FastEthernet0/2': ('10.0.2.2', '255.255.255.0')}}

Проверить работу генератора на примере конфигураций config_r1.txt и config_r2.txt.


Задание 8.2
~~~~~~~~~~~

Создать генератор read_file_in_chunks, который считывает файл по несколько строк.

Генератор ожидает как аргумент имя файла и количество строк, которые нужно считать за раз
и должен возвращать указанное количество строк одной строкой на каждой итерации.

Проверить работу генератора на примере файла config_r1.txt.

Убедиться, что если в последней итерации строк меньше, чем в указанном аргументе, не возникает исключения.

Ограничение: нельзя использовать функции из модуля itertools.

Пример использования функции:

.. code:: python

    In [1]: g = read_file_in_chunks('config_r1.txt', 10)

    In [2]: next(g)
    Out[2]: 'Current configuration : 4052 bytes\n!\n! Last configuration change at 13:13:40 UTC Tue Mar 1 2016\nversion 15.2\nno service timestamps debug uptime\nno service timestamps log uptime\nno service password-encryption\n!\nhostname PE_r1\n!\n'


Задание 8.3
~~~~~~~~~~~

Создать генератор filter_data_by_attr, который фильтрует данные на основании указанного атрибута и значения.

Аргументы генератора:

* итерируемый объект
* имя атрибута
* значение атрибута

Заменить генераторы filter_by_nexthop и filter_by_mask генератором filter_data_by_attr
в коде ниже. Проверить работу генератора на объектах Route.
Генератор не должен быть привязан к конкретным объектам, то есть должен работать не только
с экземплярами класса Route.

Пример использования функции:


.. code:: python

    In [1]: import csv
       ...: from collections import namedtuple
       ...:
       ...: f = open('rib_table.csv')
       ...: reader = csv.reader(f)
       ...:
       ...: headers = next(reader)
       ...: Route = namedtuple("Route", headers)
       ...: route_tuples = map(Route._make, reader)
       ...:

    In [2]: nhop_23 = filter_data_by_attr(route_tuples, 'nexthop', '200.219.145.23')

    In [3]: mask_20 = filter_data_by_attr(nhop_23, 'netmask', '20')

    In [4]: next(mask_20)
    Out[4]: Route(status='*>', network='23.36.48.0', netmask='20', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 2914', origin='i')

    In [5]: next(mask_20)
    Out[5]: Route(status='*>', network='23.36.64.0', netmask='20', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 1299 20940', origin='i')

Начальный код:

.. code:: python

    import csv
    from collections import namedtuple


    def filter_by_nexthop(iterable, nexthop):
        for line in iterable:
            if line[3] == nexthop:
                yield line


    def filter_by_mask(iterable, mask):
        for line in iterable:
            if line[2] == mask:
                yield line


    if __name__ == "__main__":
        with open('rib_table.csv') as f:
            reader = csv.reader(f)
            headers = next(reader)
            Route = namedtuple("Route", headers)
            route_tuples = map(Route._make, reader)

            nhop_23 = filter_by_nexthop(route_tuples, '200.219.145.23')
            mask_20 = filter_by_mask(nhop_23, '20')


Задание 8.4
~~~~~~~~~~~

Переделать код функции send_show_command_to_devices таким образом, чтобы
она была генератором и возвращала вывод с одного устройства на каждой итерации.

Переделать соответственно код, который вызывает send_show_command_to_devices
таким образом, чтобы результат, который генерирует send_show_command_to_devices
записывался в файл.

Проверить работу генератора на устройствах из файла devices.yaml.
Для этого задания нет теста!

.. code:: python

    from itertools import repeat
    from concurrent.futures import ThreadPoolExecutor

    from netmiko import ConnectHandler
    import yaml


    def send_show_command(device, command):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            prompt = ssh.find_prompt()
        return f"{prompt}{command}\n{result}\n"


    def send_show_command_to_devices(devices, command, filename, limit=3):
        with ThreadPoolExecutor(max_workers=limit) as executor:
            results = executor.map(send_show_command, devices, repeat(command))
        with open(filename, 'w') as f:
            for output in results:
                f.write(output)

    if __name__ == "__main__":
        command = "sh ip int br"
        with open('devices.yaml') as f:
            devices = yaml.load(f)
        send_show_command_to_devices(devices, command, 'result.txt')

