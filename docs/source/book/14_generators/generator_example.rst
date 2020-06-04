Пример использования генератора для обработки вывода sh cdp neighbors detail
----------------------------------------------------------------------------

Генераторы могут использоваться не только в том случае, когда надо возвращать элементы по одному.

Например, генератор get_cdp_neighbor читает файл с выводом sh cdp neighbor detail и выдает вывод частями, по одному соседу:

.. code:: python

    def get_one_neighbor(filename):
        with open(filename) as f:
            line = ''
            while True:
                while not 'Device ID' in line:
                    line = f.readline()
                neighbor = line
                for line in f:
                    if '----------' in line:
                        break
                    neighbor += line
                yield neighbor
                line = f.readline()
                if not line:
                    return


Полный скрипт выглядит таким образом (файл parse_cdp_neighbors.py):

.. code:: python

    import re
    from pprint import pprint


    def get_one_neighbor(filename):
        with open(filename) as f:
            line = ''
            while True:
                while not 'Device ID' in line:
                    line = f.readline()
                neighbor = line
                for line in f:
                    if '----------' in line:
                        break
                    neighbor += line
                yield neighbor
                line = f.readline()
                if not line:
                    return


    def parse_neighbor(output):
        regex = (
            r'Device ID: (\S+).+?'
            r' IP address: (?P<ip>\S+).+?'
            r'Platform: (?P<platform>\S+ \S+), .+?'
            r', Version (?P<ios>\S+),')

        result = {}
        match = re.search(regex, output, re.DOTALL)
        if match:
            device = match.group(1)
            result[device] = match.groupdict()
        return result

    if __name__ == "__main__":
        data = get_one_neighbor('sh_cdp_neighbors_detail.txt')
        for n in data:
            pprint(parse_neighbor(n), width=120)


Так как генератор get_cdp_neighbor выдает каждый раз вывод про одного соседа, можно проходиться по результату в цикле и передавать каждый вывод функции parse_cdp.
И конечно же, полученный результат тоже можно не собирать в один большой словарь, а передавать куда-то дальше на обработку или запись.

Результат выполнения:

.. code:: python

    $ python parse_cdp_neighbors.py
    {'SW2': {'ios': '12.2(55)SE9', 'ip': '10.1.1.2', 'platform': 'cisco WS-C2960-8TC-L'}}
    {'R1': {'ios': '12.4(24)T1', 'ip': '10.1.1.1', 'platform': 'Cisco 3825'}}
    {'R2': {'ios': '15.2(2)T1', 'ip': '10.2.2.2', 'platform': 'Cisco 2911'}}
    {'R3': {'ios': '15.2(2)T1', 'ip': '10.3.3.3', 'platform': 'Cisco 2911'}}

