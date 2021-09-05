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

Отсутствие проверки None
~~~~~~~~~~~~~~~~~~~~~~~~

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

Особенности работы с Union
~~~~~~~~~~~~~~~~~~~~~~~~~~

Пример кода, в котором в значении словаря типы указаны как Union[str, int, bool] (полный пример в файле example_14_dict_multiple_types_wrong.py):

.. code:: python

    def send_show_command_to_devices(
        devices: List[Dict[str, Union[str, int, bool]]], command: str
    ) -> Dict[str, str]:
        data = {}
        for device in devices:
            output = send_show_command(device, command)
            data[device["host"]] = output
        return data

В этом случае возникнет такая ошибка:

::

    $ mypy example_14_dict_multiple_types.py
    example_14_dict_multiple_types_wrong.py:24: error: Incompatible return value type (got "Dict[Union[str, int, bool], str]", expected "Dict[str, str]")
    Found 1 error in 1 file (checked 1 source file)

Проблема связана с тем, что если в значении словаря указан ``Union[str, int, bool]``, то mypy это воспринимает как то, что любое
значение может быть любым из этих типов. Указав что результатом будет словарь ``Dict[str, str]``. Мы как бы уточняем, что ``device["host"]``
соответствует именно строка, но при работе с Union это будет ошибкой.
Исправить ошибку можно либо указав, что возвращаемый словарь будет содержать в ключе ``Union[str, int, bool]``, или указав в словаре
в devices тип значения ``Any`` (полный пример в example_14_dict_multiple_types.py):

.. code:: python

    def send_show_command_to_devices(
        devices: List[Dict[str, Any]], command: str
    ) -> Dict[str, str]:
        data = {}
        for device in devices:
            output = send_show_command(device, command)
            data[device["host"]] = output
        return data


