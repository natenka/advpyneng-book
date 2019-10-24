Конечные итераторы
------------------

zip_longest
~~~~~~~~~~~

Функция zip_longest работает аналогично встроенной функции zip,
но не останавливается на самом коротком итерируемом объекте.

.. code:: python

    itertools.zip_longest(*iterables, fillvalue=None)

Пример использования:

.. code:: python

    In [20]: list(zip([1,2,3,4,5], [10,20]))
    Out[20]: [(1, 10), (2, 20)]

    In [21]: list(zip_longest([1,2,3,4,5], [10,20]))
    Out[21]: [(1, 10), (2, 20), (3, None), (4, None), (5, None)]

    In [22]: list(zip_longest([1,2,3,4,5], [10,20], fillvalue=0))
    Out[22]: [(1, 10), (2, 20), (3, 0), (4, 0), (5, 0)]

chain
~~~~~

Функция chain ожидает несколько итерируемых объектов как аргумент и возвращает
единый итератор, который перебирает элементы каждого итерируемого объекта
так, как будто они составляют единый объект:

.. code:: python

    itertools.chain(*iterables)

Пример использования:

.. code:: python

    In [4]: line = 'test'

    In [5]: items = [1, 2, 3]

    In [6]: mapping = {'ios': '15.4', 'vendor': 'Cisco'}

    In [7]: for item in chain(line, items, mapping):
       ...:     print(item)
       ...:
    t
    e
    s
    t
    1
    2
    3
    ios
    vendor

compress
~~~~~~~~

Функция compress позволяет фильтровать данные: она возвращает те элементы из data, которые
соответветствуют истинному значению в selectors:

.. code:: python

    itertools.compress(data, selectors)

Пример использования compress для фильтрации полей с ненулевым значением:

.. code:: python

    In [9]: headers = ['tx_packets', 'rx_packets', 'tx_bytes', 'rx_bytes', 'broadcasts']

    In [10]: data = [294785, 0, 22275381, 0, 253218]

    In [12]: list(compress(headers, data))
    Out[12]: ['tx_packets', 'tx_bytes', 'broadcasts']

    In [14]: list(compress(zip(headers, data), data))
    Out[14]: [('tx_packets', 294785), ('tx_bytes', 22275381), ('broadcasts', 253218)]

    n [24]: dict(compress(zip(headers, data), data))
    Out[24]: {'tx_packets': 294785, 'tx_bytes': 22275381, 'broadcasts': 253218}

tee
~~~

Функция tee создает несколько независимых итераторов на основе исходных данных:

.. code:: python

    itertools.tee(iterable, n=2)

Пример использования:

.. code:: python

    In [30]: data = [1,2,3,4,5,6]

    In [31]: data_iter = iter(data)

    In [32]: duplicate_1, duplicate_2 = tee(data_iter)

    In [33]: list(duplicate_1)
    Out[33]: [1, 2, 3, 4, 5, 6]

    In [34]: list(duplicate_2)
    Out[34]: [1, 2, 3, 4, 5, 6]

Важная особенность tee - исходный итератор лучше не использовать,
иначе полученные итераторы начнут перебор не с начала:

.. code:: python

    In [35]: data_iter = iter(data)

    In [36]: duplicate_1, duplicate_2 = tee(data_iter)

    In [37]: next(data_iter)
    Out[37]: 1

    In [38]: next(data_iter)
    Out[38]: 2

    In [39]: list(duplicate_1)
    Out[39]: [3, 4, 5, 6]

    In [40]: list(duplicate_2)
    Out[40]: [3, 4, 5, 6]

При этом перебор одной копии, не влияет на вторую:

.. code:: python

    In [41]: data_iter = iter(data)

    In [42]: duplicate_1, duplicate_2 = tee(data_iter)

    In [43]: next(duplicate_1)
    Out[43]: 1

    In [44]: next(duplicate_1)
    Out[44]: 2

    In [45]: list(duplicate_1)
    Out[45]: [3, 4, 5, 6]

    In [46]: list(duplicate_2)
    Out[46]: [1, 2, 3, 4, 5, 6]


islice
~~~~~~

Функция islice


groupby
~~~~~~~

Функция groupby



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



