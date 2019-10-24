dropwhile и takewhile
~~~~~~~~~~~~~~~~~~~~~

Функция dropwhile ожидает как аргументы функцию, которая возвращает True или False, в зависимости от условия, и итерируемый объект.
Функция dropwhile отбрасывает элементы итерируемого объекта до тех пор, пока функция переданная как аргумент возвращает True.
Как только dropwhile встречает False, он возвращает итератор с оставшимися объектами.

.. code:: python

    In [1]: from itertools import dropwhile

    In [2]: list(dropwhile(lambda x: x < 5, [0,2,3,5,10,2,3]))
    Out[2]: [5, 10, 2, 3]


В данном случае, как только функция dropwhile дошла до числа, которое больше или равно пяти, она вернула все оставшиеся числа.
При этом, даже если далее есть числа, которые меньше 5, функция уже не проверяет их.


Функция takewhile - противоположность функции dropwhile: она возвращает итератор
с теми элементами, которые соответствуют условию, до первого ложного условия:

.. code:: python

    In [3]: from itertools import takewhile

    In [4]: list(takewhile(lambda x: x < 5, [0,2,3,5,10,2,3]))
    Out[4]: [0, 2, 3]


Пример использования takewhile и dropwhile

.. code:: python

    def get_cdp_neighbor(sh_cdp_neighbor_detail):
        with open(sh_cdp_neighbor_detail) as f:
            while True:
                begin = dropwhile(lambda x: not 'Device ID' in x, f)
                lines = takewhile(lambda y: not '-----' in y, begin)
                neighbor = ''.join(lines)
                if not neighbor:
                    return
                yield neighbor


Файл parse_cdp_file.py:

.. code:: python

    import re
    from pprint import pprint
    from itertools import dropwhile, takewhile


    def get_cdp_neighbor(sh_cdp_neighbor_detail):
        with open(sh_cdp_neighbor_detail) as f:
            while True:
                f = dropwhile(lambda x: not 'Device ID' in x, f)
                lines = takewhile(lambda y: not '-----' in y, f)
                neighbor = ''.join(lines)
                if not neighbor:
                    return None
                yield neighbor


    def parse_cdp_neighbor(output):
        regex = ('Device ID: (\S+)\n.*?'
                 ' +IP address: (?P<ip>\S+).+?'
                 'Platform: (?P<platform>\S+ \S+),.+?'
                 'Version (?P<ios>\S+),')

        result = {}
        match = re.search(regex, output, re.DOTALL)
        if match:
            device = match.group(1)
            result[device] = match.groupdict()
        return result


    def parse_cdp_output(filename):
        result = get_cdp_neighbor(filename)
        all_cdp = {}
        for neighbor in result:
            all_cdp.update(parse_cdp_neighbor(neighbor))
        return all_cdp


    if __name__ == "__main__":
        filename = 'sh_cdp_neighbors_detail.txt'
        pprint(parse_cdp_output(filename), width=120)


Результат:

.. code:: python

    $ python parse_cdp_file.py
    {'R1': {'ios': '12.4(24)T1', 'ip': '10.1.1.1', 'platform': 'Cisco 3825'},
     'R2': {'ios': '15.2(2)T1', 'ip': '10.2.2.2', 'platform': 'Cisco 2911'},
     'R3': {'ios': '15.2(2)T1', 'ip': '10.3.3.3', 'platform': 'Cisco 2911'},
     'SW2': {'ios': '12.2(55)SE9', 'ip': '10.1.1.2', 'platform': 'cisco WS-C2960-8TC-L'}}

