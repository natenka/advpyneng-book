Пример использования генератора для обработки вывода sh cdp neighbors detail
----------------------------------------------------------------------------

Генераторы могут использоваться не только в том случае, когда надо возвращать элементы по одному.

Например, генератор get_cdp_neighbor читает файл с выводом sh cdp neighbor detail и выдает вывод частями, по одному соседу:

.. code:: python

    def get_cdp_neighbor(sh_cdp_neighbor_detail):
        with open(sh_cdp_neighbor_detail) as f:
            line = ''
            while True:
                while not 'Device ID' in line:
                    line = f.readline()
                neighbor = ''
                neighbor += line
                for line in f:
                    if line.startswith('-----'):
                        break
                    neighbor += line
                yield neighbor
                line = f.readline()
                if not line:
                    return


Полный скрипт выглядит таким образом (файл parse_cdp_file.py):

.. code:: python

    import re
    from pprint import pprint

    def get_cdp_neighbor(sh_cdp_neighbor_detail):
        with open(sh_cdp_neighbor_detail) as f:
            line = ''
            while True:
                while not 'Device ID' in line:
                    line = f.readline()
                neighbor = ''
                neighbor += line
                for line in f:
                    if line.startswith('-----'):
                        break
                    neighbor += line
                yield neighbor
                line = f.readline()
                if not line:
                    return


    def parse_cdp(output):
        regex = ('Device ID: (?P<device>\S+)'
                 '|IP address: (?P<ip>\S+)'
                 '|Platform: (?P<platform>\S+ \S+),'
                 '|Cisco IOS Software, (?P<ios>.+), RELEASE')

        result = {}

        match_iter = re.finditer(regex, output)
        for match in match_iter:
            if match.lastgroup == 'device':
                device = match.group(match.lastgroup)
                result[device] = {}
            elif device:
                result[device][match.lastgroup] = match.group(match.lastgroup)

        return result


    filename = 'sh_cdp_neighbors_detail.txt'
    result = get_cdp_neighbor(filename)

    all_cdp = {}
    for cdp in result:
        all_cdp.update(parse_cdp(cdp))

    pprint(all_cdp)


Так как генератор get_cdp_neighbor выдает каждый раз вывод про одного соседа, можно проходиться по результату в цикле и передавать каждый вывод функции parse_cdp.
И конечно же, полученный результат тоже можно не собирать в один большой словарь, а передавать куда-то дальше на обработку или запись.

Результат выполнения:

.. code:: python

    $ python parse_cdp_file.py
    {'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
            'ip': '10.1.1.1',
            'platform': 'Cisco 3825'},
     'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
            'ip': '10.2.2.2',
            'platform': 'Cisco 2911'},
     'R3': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
            'ip': '10.3.3.3',
            'platform': 'Cisco 2911'},
     'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
             'ip': '10.1.1.2',
             'platform': 'cisco WS-C2960-8TC-L'}}

