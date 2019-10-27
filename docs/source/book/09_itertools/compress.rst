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

    In [24]: dict(compress(zip(headers, data), data))
    Out[24]: {'tx_packets': 294785, 'tx_bytes': 22275381, 'broadcasts': 253218}

Пример фильтрации None:

.. code:: python

    In [25]: data2
    Out[25]: [294785, 0, 22275381, None, None]

    In [26]: headers
    Out[26]: ['tx_packets', 'rx_packets', 'tx_bytes', 'rx_bytes', 'broadcasts']

    In [27]: list(compress(zip(headers, data2), selectors=map(lambda x: x != None, data2)))
    Out[27]: [('tx_packets', 294785), ('rx_packets', 0), ('tx_bytes', 22275381)]
