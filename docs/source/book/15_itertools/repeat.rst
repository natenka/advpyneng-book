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


