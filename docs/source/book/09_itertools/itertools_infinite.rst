Бесконечные итераторы
---------------------


repeat
~~~~~~

Функция repeat возвращает итератор, который повторяет указанный объект
бесконечно или указанное количество раз:

.. code:: python

    itertools.repeat(object[, times])

Пример использования repeat для повторения команды:

.. code:: python

    from itertools import repeat
    from concurrent.futures import ThreadPoolExecutor

    import netmiko
    import yaml


    def send_show(device, show):
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show)
            return result


    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)

    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(send_show, devices, repeat('sh clock'))
        for device, output in zip(devices, result):
            print(device['ip'], output)


cicle
~~~~~

Функция cycle создает итератор, которые возвращает элементы итерируемого объекта по кругу:

.. code:: python

    itertools.cycle(iterable)

Пример использования cycle:

.. code:: python

    from itertools import cycle


    spinner = it.cycle('\|/-')
    for _ in range(20):
        print(f'\r{next(spinner)}', end='')
        time.sleep(0.5)


count
~~~~~

Функция count возвращает итератор, который генерирует числа бесконечно, начиная с указанного
в start и используя шаг step:

.. code:: python

    itertools.count(start=0, step=1)


Пример использования count:

.. code:: python

    from itertools import count


    In [13]: ip_list
    Out[13]:
    ['192.168.100.1',
     '192.168.100.2',
     '192.168.100.3',
     '192.168.100.4',
     '192.168.100.5']

    In [18]: for num, ip in zip(count(1), ip_list):
        ...:     print((num, ip))
        ...:
    (1, '192.168.100.1')
    (2, '192.168.100.2')
    (3, '192.168.100.3')
    (4, '192.168.100.4')
    (5, '192.168.100.5')


