dropwhile и takewhile
---------------------

В Python есть отдельный модуль itertools в котором находятся итераторы и средства работы с ними.

Используя функции dropwhile и takewhile из модуля itertools, можно значительно сократить код в функции get_cdp_neighbor.


Функция dropwhile ожидает как аргументы функцию, которая возвращает True или False, в зависимости от условия, и итерируемый объект.
Функция dropwhile отбрасывает элементы итерируемого объекта до тех пор, пока функция переданная как аргумент возвращает True.
Как только dropwhile встречает False, он возвращает итератор с оставшимися объектами.

Пример:
.. code:: python

    In [1]: from itertools import dropwhile

    In [2]: list(dropwhile(lambda x: x < 5, [0,2,3,5,10,2,3]))
    Out[2]: [5, 10, 2, 3]


В данном случае, как только функция dropwhile дошла до числа, которое больше или равно пяти, она вернула все оставшиеся числа.
При этом, даже если далее есть числа, которые меньше 5, функция уже не проверяет их.

takewhile
~~~~~~~~~

Функция takewhile є абсолютная противоположность функции dropwhile: она возвращает итератор с теми элементами, которые соответствуют условию, до первого ложного условия:

.. code:: python

    In [3]: from itertools import takewhile

    In [4]: list(takewhile(lambda x: x < 5, [0,2,3,5,10,2,3]))
    Out[4]: [0, 2, 3]



Пример использования takewhile и dropwhile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Генератор get_cdp_neighbor, который использовался ранее, возвращает вывод sh cdp neighbors detail по одному соседу.

Логика функции была такая:

* сначала надо отбросить все, пока не встретится строка с Device ID
* затем надо взять все строки, пока не встретится строка с '-----'
* потом начать все с начала

В прошлом варианте эта функциональность реализована циклами.
Но первое условие - это именно то, что делает функция dropwhile, а второе - то, что делает функция takewhile.

В итоге, генератор выглядит так:

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


Остальные части скрипта никак не поменялись (файл parse_cdp_file_ver2.py):

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
                    return
                yield neighbor


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



Результат аналогичный:

::

$ python parse_cdp_file_ver2.py

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



