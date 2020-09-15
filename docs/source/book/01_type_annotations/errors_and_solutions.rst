Ошибки и решения
----------------

Ошибки при использовании type вместо isinstance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При использовании type для создания условия по типу данных таким образом:

.. code:: python

    from netmiko import ConnectHandler
    from typing import Dict, Union, Iterable, Any


    def send_show_commands(
        device_params: Dict[str, Any], commands: Union[str, Iterable[str]]
    ) -> Dict[str, str]:
        result = {}
        if type(commands) == str:
            commands = [commands]
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result

Mypy выдаст такую ошибку:

::

    $ mypy example_16_isinstance.py
    example_16_isinstance.py:11: error: List item 0 has incompatible type "Union[str, Iterable[str]]"; expected "str"
    Found 1 error in 1 file (checked 1 source file)

Исправить ситуацию можно таким образом:

.. code:: python

    def send_show_commands(
        device_params: Dict[str, Any], commands: Union[str, Iterable[str]]
    ) -> Dict[str, str]:
        result = {}
        if isinstance(commands, str):
            commands = [commands]
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result

