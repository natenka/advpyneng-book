Создание классов с помощью namedtuple
-------------------------------------


collections.namedtuple
~~~~~~~~~~~~~~~~~~~~~~

Функция namedtuple позволяет создавать новые классы, которые наследуют tuple и при этом:

* доступ к атрибутам может осуществляться по имени
* доступ к элементами по индексу
* экземпляр класса является итерируемым объектом
* атрибуты неизменяемы

Именованные кортежи присваивают имена каждому элементу кортежа
и код выглядит более понятным, так как вместо индексов используются имена.
При этом, все возможности обычных кортежей остаются.


.. code:: python

    In [1]: from collections import namedtuple

    In [2]: RouterClass = namedtuple('Router', ['hostname', 'ip', 'ios'])

    In [3]: r1 = RouterClass('r1', '10.1.1.1', '15.4')

    In [30]: r1
    Out[30]: Router(hostname='r1', ip='10.1.1.1', ios='15.4')


    In [18]: r1.hostname
    Out[18]: 'r1'

    In [19]: r1.ip
    Out[19]: '10.1.1.1'

    In [20]: hostname, ip, ios = r1

    In [21]: hostname
    Out[21]: 'r1'

    In [22]: ip
    Out[22]: '10.1.1.1'

    In [23]: ios
    Out[23]: '15.4'


Метод _as_dict возвращает OrderedDict:

.. code:: python

    In [9]: r1._asdict()
    Out[9]: OrderedDict([('hostname', 'r1'), ('ip', '10.1.1.1'), ('ios', '15.4')])

Метод _replace возвращает новый экземпляр класса, в котором заменены указанные поля:

.. code:: python

    In [18]: r1 = RouterClass('r1', '10.1.1.1', '15.4')

    In [19]: r1
    Out[19]: Router(hostname='r1', ip='10.1.1.1', ios='15.4')

    In [20]: r1._replace(ip='10.2.2.2')
    Out[20]: Router(hostname='r1', ip='10.2.2.2', ios='15.4')

Метод _make создает новый экземпляр класса из последовательности полей (это метод класса):

.. code:: python

    In [22]: RouterClass._make(['r3', '10.3.3.3', '15.2'])
    Out[22]: Router(hostname='r3', ip='10.3.3.3', ios='15.2')

    In [23]: r3 = RouterClass._make(['r3', '10.3.3.3', '15.2'])


Пример использования namedtuple:

.. code:: python

    import sqlite3
    from collections import namedtuple


    key = 'vlan'
    value = 10
    db_filename = 'dhcp_snooping.db'

    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    DhcpSnoopRecord = namedtuple('DhcpSnoopRecord', keys)

    conn = sqlite3.connect(db_filename)
    query = 'select {} from dhcp where {} = ?'.format(','.join(keys), key)

    print('-' * 40)
    for row in map(DhcpSnoopRecord._make, conn.execute(query, (value,))):
        print(row.mac, row.ip, row.interface, sep='\n')
        print('-' * 40)

Вывод:

::

    $ python get_data.py
    ----------------------------------------
    00:09:BB:3D:D6:58
    10.1.10.2
    FastEthernet0/1
    ----------------------------------------
    00:07:BC:3F:A6:50
    10.1.10.6
    FastEthernet0/3
    ----------------------------------------

Параметр defaults позволяет указывать значения по умолчанию:

.. code:: python

    In [33]: IPAddress = namedtuple('IPAddress', ['address', 'mask'], defaults=[24])

    In [34]: ip1 = IPAddress('10.1.1.1', 28)

    In [35]: ip1
    Out[35]: IPAddress(address='10.1.1.1', mask=28)

    In [36]: ip2 = IPAddress('10.2.2.2')

    In [37]: ip2
    Out[37]: IPAddress(address='10.2.2.2', mask=24)


typing.NamedTuple
~~~~~~~~~~~~~~~~~

Еще один вариант создания класса с помощью именнованного кортежа - наследование
класса typing.NamedTuple.
Базовые особенности namedtuple сохраняются, плюс есть возможность добавлять свои методы.

.. code:: python

    classs IPAddress(typing.NamedTuple):
        pass

    In [33]: IPAddress = namedtuple('IPAddress', ['address', 'mask'], defaults=[24])

    In [34]: ip1 = IPAddress('10.1.1.1', 28)

    In [35]: ip1
    Out[35]: IPAddress(address='10.1.1.1', mask=28)

    In [36]: ip2 = IPAddress('10.2.2.2')

    In [37]: ip2
    Out[37]: IPAddress(address='10.2.2.2', mask=24)

