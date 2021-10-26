NullHandler
-----------

.. code:: python

    import logging


    log = logging.getLogger(__name__)
    log.addHandler(logging.NullHandler())


    def send_show(device_dict, command):
        ip = device_dict["host"]
        log.info(f"===>  Connection: {ip}")

        try:
            with ConnectHandler(**device_dict) as ssh:
                ssh.enable()
                result = ssh.send_command(command)
                log.debug(f"<===  Received:   {ip}")
                log.debug(f"Получен вывод команды {command}\n\n{result}")
            return result
        except SSHException as error:
            log.error(f"Ошибка {error} на {ip}")
