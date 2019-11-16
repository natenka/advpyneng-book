Базовый пример
--------------

logging_basic_1.py

.. code:: python

    import logging

    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)

    logging.debug('Сообщение уровня debug')
    logging.info('Сообщение уровня info')
    logging.warning('Сообщение уровня warning')

Log-файл

::
    DEBUG:root:Сообщение уровня debug
    INFO:root:Сообщение уровня info
    WARNING:root:Сообщение уровня warning

logging_basic_2.py

.. code:: python


    import logging

    logging.basicConfig(filename='mylog2.log', level=logging.DEBUG)

    logging.debug('Сообщение уровня debug:\n%s', str(globals()))
    logging.info('Сообщение уровня info')
    logging.warning('Сообщение уровня warning')


Log-файл

::

    DEBUG:root:Сообщение уровня debug:
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0xb72a57ac>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'logging_basic_2.py', '__cached__': None, 'logging': <module 'logging' from '/usr/local/lib/python3.6/logging/__init__.py'>}
    INFO:root:Сообщение уровня info
    WARNING:root:Сообщение уровня warning


Пример вывода информации о потоках:

.. code:: python

    from concurrent.futures import ThreadPoolExecutor
    from pprint import pprint
    from datetime import datetime
    import time
    from itertools import repeat
    import logging
    import yaml
    from netmiko import ConnectHandler, NetMikoAuthenticationException


    logging.getLogger('paramiko').setLevel(logging.WARNING)

    logging.basicConfig(
        format='%(threadName)s %(name)s %(levelname)s: %(message)s',
        level=logging.INFO)


    def send_show(device_dict, command):
        ip = device_dict['host']
        logging.info(f'===> {datetime.now().time()} Connection: {ip}')
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            logging.info(f'<=== {datetime.now().time()} Received:   {ip}')
        return result


    def send_command_to_devices(devices, command):
        data = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            result = executor.map(send_show, devices, repeat(command))
            for device, output in zip(devices, result):
                data[device['host']] = output
        return data


    if __name__ == '__main__':
        with open('devices.yaml') as f:
            devices = yaml.safe_load(f)
        pprint(send_command_to_devices(devices, 'sh ip int br'), width=120)

