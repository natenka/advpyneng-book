Компоненты модуля logging
-------------------------

* Logger - это основной интерфейс для работы с модулем
* Handler - отправляет log-сообщения конкретному получателю
* Filter - позволяет фильтровать сообщения
* Formatter - указывает формат сообщения


Вывод на стандартный поток ошибок logging_api_example_1.py

.. code:: python

    import logging

    logger = logging.getLogger(__name__)

    ## messages
    logger.debug('Сообщение уровня debug')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


Результат выполнения

::

    $ python logging_api_example_1.py
    Сообщение уровня warning


logging_api_example_2.py

.. code:: python

    import logging

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)

    logger.addHandler(console)

    ## messages
    logger.debug('Сообщение уровня debug %s', 'SOS')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


Результат выполнения

::

    $ python logging_api_example_2.py
    16:39:27 - My Script - DEBUG - Сообщение уровня debug: SOS
    16:39:27 - My Script - INFO - Сообщение уровня info
    16:39:27 - My Script - WARNING - Сообщение уровня warning

Вывод на стандартный поток вывода logging_api_example_2_stdout.py

.. code:: python

    import sys
    import logging

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)

    logger.addHandler(console)

    ## messages
    logger.debug('Сообщение уровня debug %s', 'SOS')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


logging_api_example_2_new_format.py

.. code:: python

    import logging

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                                  datefmt='%H:%M:%S', style='{')
    console.setFormatter(formatter)

    logger.addHandler(console)

    ## messages
    logger.debug('Сообщение уровня debug: %s', 'SOS')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


Результат выполнения

::

    $ python logging_api_example_2.py
    16:45:20 - My Script - DEBUG - Сообщение уровня debug: SOS
    16:45:20 - My Script - INFO - Сообщение уровня info
    16:45:20 - My Script - WARNING - Сообщение уровня warning



Запись логов в файл
-------------------

logging_api_example_3.py

.. code:: python

    import logging

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    logfile = logging.FileHandler('logfile.log')
    logfile.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    logfile.setFormatter(formatter)

    logger.addHandler(logfile)

    ## messages
    logger.debug('Сообщение уровня debug')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')




Результат выполнения. Файл logfile.log

::

    17:58:34 - My Script - WARNING - Сообщение уровня warning




Запись в файл и вывод на stderr
-------------------------------

logging_api_example_4.py

.. code:: python

    import logging

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    ### stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                                  datefmt='%H:%M:%S', style='{')
    console.setFormatter(formatter)

    logger.addHandler(console)

    ### File
    logfile = logging.FileHandler('logfile3.log')
    logfile.setLevel(logging.WARNING)
    formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                                  datefmt='%H:%M:%S', style='{')
    logfile.setFormatter(formatter)

    logger.addHandler(logfile)

    ## messages
    logger.debug('Сообщение уровня debug')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


Handlers
--------

RotatingFileHandler
~~~~~~~~~~~~~~~~~~~

logging_api_example_5_file_rotation.py

.. code:: python

    import logging
    import logging.handlers

    logger = logging.getLogger('My Script')
    logger.setLevel(logging.DEBUG)

    logfile = logging.handlers.RotatingFileHandler(
        'logfile_with_rotation.log', maxBytes=10, backupCount=3)
    logfile.setLevel(logging.DEBUG)
    formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                                  datefmt='%H:%M:%S', style='{')
    logfile.setFormatter(formatter)

    logger.addHandler(logfile)

    ## messages
    logger.debug('Сообщение уровня debug')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')

Результат выполнения

::

    $ ls -1 logfile_with_rotation*
    logfile_with_rotation.log
    logfile_with_rotation.log.1
    logfile_with_rotation.log.2
    logfile_with_rotation.log.3
    logfile_with_rotation.log - это самый свежий файл, затем идет logfile_with_rotation.log.1, logfile_with_rotation.log.2 и тд.


Logging tree
------------


netmiko_func.py

.. code:: python


    import logging
    from netmiko import ConnectHandler


    logger = logging.getLogger('superscript.netfunc')
    #logger = logging.getLogger('netfunc')

    device_params = {
         'device_type': 'cisco_ios',
         'ip': '192.168.100.1',
         'username': 'cisco',
         'password': 'cisco',
         'secret': 'cisco'}


    def send_show_command(device, command):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            logger.debug('Вывод команды:\n{}'.format(output))
        return output

    if __name__ == '__main__':
        send_show_command(device_params, 'sh ip int br')

logging_api_example_6_mult_files.py

.. code:: python

    import logging
    from netmiko_func import send_show_command, device_params

    logger = logging.getLogger('superscript')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)

    logger.addHandler(console)

    if __name__ == "__main__":
        logger.debug('Before function')
        send_show_command(device_params, 'sh ip int br')
        logger.debug('After function')




Результат выполнения

::

    $ python logging_api_example_6_mult_files.py
    19:16:44 - superscript - DEBUG - Before function
    19:16:50 - superscript.netfunc - DEBUG - Вывод команды:
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
    Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
    Ethernet0/3                192.168.230.1   YES NVRAM  administratively down down
    Ethernet0/3.100            10.100.0.1      YES NVRAM  administratively down down
    Ethernet0/3.200            10.200.0.1      YES NVRAM  administratively down down
    Ethernet0/3.300            10.30.0.1       YES NVRAM  administratively down down
    Loopback0                  10.1.1.2        YES manual up                    up
    19:16:50 - superscript - DEBUG - After function


logger.exception
----------------

logging_api_example_7_exception.py

.. code:: python

    import logging
    from netmiko_func import send_show_command, device_params

    logger = logging.getLogger('superscript')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)

    logger.addHandler(console)

    logger.debug('Before exception')
    try:
        2 + 'test'
    except TypeError:
        logger.exception('Error')
    logger.debug('After exception')

Результат выполнения

::

    $ python logging_api_example_7_exception.py
    19:23:24 - superscript - DEBUG - Before exception
    19:23:24 - superscript - ERROR - Error
    Traceback (most recent call last):
      File "logging_api_example_7_exception.py", line 17, in <module>
        2 + 'test'
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    19:23:24 - superscript - DEBUG - After exception

Конфигурация logging из словаря
-------------------------------


logging_api_example_8.py

.. code:: python

    import logging

    logger = logging.getLogger('superscript')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)

    logger.addHandler(console)

    ## messages
    logger.debug('Сообщение уровня debug %s', 'SOS')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


logging_api_example_8_yaml_cfg.py

.. code:: python

    import logging
    import logging.config
    import yaml

    # create logger
    logger = logging.getLogger('superscript')

    #read config
    with open('log_config.yml') as f:
        log_config = yaml.load(f)

    logging.config.dictConfig(log_config)

    ## messages
    logger.debug('Сообщение уровня debug %s', 'SOS')
    logger.info('Сообщение уровня info')
    logger.warning('Сообщение уровня warning')


log_config.yml

.. code:: yaml

    version: 1
    formatters:
      simple:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
      console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    loggers:
      superscript:
        level: DEBUG
        handlers: [console]
        propagate: no
    root:
      level: DEBUG
      handlers: [console]

::

    $python logging_api_example_8_yaml_cfg.py
    2018-02-17 19:50:56,266 - superscript - DEBUG - Сообщение уровня debug SOS
    2018-02-17 19:50:56,266 - superscript - INFO - Сообщение уровня info
    2018-02-17 19:50:56,266 - superscript - WARNING - Сообщение уровня warning
