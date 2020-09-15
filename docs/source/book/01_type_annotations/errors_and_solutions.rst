Ошибки и решения
----------------

Ошибки при использовании type вместо isinstance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Это известная проблема https://github.com/python/mypy/issues/4445

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

Исправить ситуацию можно используя isinstance вместо type:

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

Отстутствие проверки None
~~~~~~~~~~~~~~~~~~~~~~~~~

Пример кода:

.. code:: python

    import re
    from typing import List, Tuple


    def parse_sh_cdp_neighbors(command_output: str) -> List[Tuple[str, ...]]:
        regex = re.compile(
            r"(?P<r_dev>\w+) +(?P<l_intf>\S+ \S+)"
            r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
        )
        connect_list = []
        match_l_dev = re.search(r"(\S+)[>#]", command_output)
        l_dev = match_l_dev.group(1)
        for match in regex.finditer(command_output):
            neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
            connect_list.append(neighbor)
        return connect_list

При таком коде mypy выдаст ошибку:

::

    $ mypy example_17_re_search.py
    example_17_re_search.py:13: error: Item "None" of "Optional[Match[str]]" has no attribute "group"
    Found 1 error in 1 file (checked 1 source file)

Ошибка возникает потому что выражение ``match_l_dev = re.search(r"(\S+)[>#]", command_output)`` может возвращать
None или объект Match. Без проверки что возвращается именно истинное значение, будет ошибка. Код надо исправить таким образом:

.. code:: python

    def parse_sh_cdp_neighbors(command_output: str) -> List[Tuple[str, ...]]:
        regex = re.compile(
            r"(?P<r_dev>\w+) +(?P<l_intf>\S+ \S+)"
            r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
        )
        connect_list = []
        match_l_dev = re.search(r"(\S+)[>#]", command_output)
        if match_l_dev:
            l_dev = match_l_dev.group(1)
        for match in regex.finditer(command_output):
            neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
            connect_list.append(neighbor)
        return connect_list

