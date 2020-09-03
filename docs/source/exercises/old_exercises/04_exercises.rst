.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst


Задание 4.1
~~~~~~~~~~~~

Создать класс CiscoTelnet, который наследует класс TelnetBase из файла base_telnet_class.py.

Переписать метод __init__ в классе CiscoTelnet таким образом:

* добавить параметры:

 * enable - пароль на режим enable
 * disable_paging - отключает постраничный вывод команд, по умолчанию равен True

* после подключения по Telnet должен выполняться переход в режим enable:
  для этого в методе __init__ должен сначала вызываться метод __init__ класса TelnetBase,
  а затем выполняться переход в режим enable.

Добавить в класс CiscoTelnet метод send_show_command, который отправляет команду
show и возвращает ее вывод в виде строки. Метод ожидает как аргумент одну команду.

Добавить в класс CiscoTelnet метод send_config_commands, который отправляет одну
или несколько команд на оборудование в конфигурационном режиме и возвращает ее
вывод в виде строки. Метод ожидает как аргумент одну команду (строку) или
несколько команд (список).

Пример работы класса:

.. code:: python

    In [1]: r1 = CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco')

    Метод send_show_command:
    In [2]: r1.send_show_command('sh clock')
    Out[2]: 'sh clock\r\n*09:39:38.633 UTC Thu Oct 10 2019\r\nR1#'

    Метод send_config_commands:
    In [3]: r1.send_config_commands('logging 7.7.7.7')
    Out[3]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 7.7.7.7\r\nR1(config)#end\r\nR1#'

    In [4]: r1.send_config_commands(['interface loop77', 'ip address 107.7.7.7 255.255.255.255'])
    Out[4]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop77\r\nR1(config-if)#ip address 107.7.7.7 255.255.255.255\r\nR1(config-if)#end\r\nR1#'


Задание 4.1a
~~~~~~~~~~~~

Скопировать класс CiscoTelnet из задания 4.1 и добавить проверку на ошибки.

Добавить метод _check_error_in_command, который выполняет проверку на такие ошибки:

* Invalid input detected, Incomplete command, Ambiguous command

Создать исключение ErrorInCommand, которое будет генерироваться при возникновении
ошибки на оборудовании.

Метод ожидает как аргумент команду и вывод команды. Если в выводе не обнаружена ошибка,
метод ничего не возвращает. Если в выводе найдена ошибка, метод генерирует исключение
ErrorInCommand с сообщением о том какая ошибка была обнаружена, на каком устройстве и в какой команде.

Добавить проверку на ошибки в методы send_show_command и send_config_commands.

Пример работы класса с ошибками:

.. code:: python

    In [1]: r1 = CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco')

    In [2]: r1.send_show_command('sh clck')
    ---------------------------------------------------------------------------
    ErrorInCommand                            Traceback (most recent call last)
    <ipython-input-2-e26d712f3ad3> in <module>
    ----> 1 r1.send_show_command('sh clck')
    ...
    ErrorInCommand: При выполнении команды "sh clck" на устройстве 192.168.100.1 возникла ошибка "Invalid input detected at '^' marker.

    In [3]: r1.send_config_commands('loggg 7.7.7.7')
    ---------------------------------------------------------------------------
    ErrorInCommand                            Traceback (most recent call last)
    <ipython-input-3-ab4a1ce52554> in <module>
    ----> 1 r1.send_config_commands('loggg 7.7.7.7')
    ...
    ErrorInCommand: При выполнении команды "loggg 7.7.7.7" на устройстве 192.168.100.1 возникла ошибка "Invalid input detected at '^' marker.

Без ошибок:

.. code:: python

    In [4]: r1.send_show_command('sh clock')
    Out[4]: 'sh clock\r\n*09:39:38.633 UTC Thu Oct 10 2019\r\nR1#'

    In [5]: r1.send_config_commands('logging 7.7.7.7')
    Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 7.7.7.7\r\nR1(config)#end\r\nR1#'

    In [6]: r1.send_config_commands(['interface loop77', 'ip address 107.7.7.7 255.255.255.255'])
    Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop77\r\nR1(config-if)#ip address 107.7.7.7 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

Примеры команд с ошибками:

::

    R1(config)#logging 0255.255.1
                       ^
    % Invalid input detected at '^' marker.
    R1(config)#logging
    % Incomplete command.

    R1(config)#sh i
    % Ambiguous command:  "sh i"



Задание 4.2
~~~~~~~~~~~

Скопировать класс IPv4Network из задания 3.1 и изменить его таким
образом, чтобы класс IPv4Network наследовал абстрактный класс Sequence.
Создать все необходимые абстрактные методы для работы IPv4Network как Sequence.

Проверить, что работают все методы характерные для последовательности (sequence):

* __getitem__, __len__, __contains__, __iter__, index, count

Пример создания экземпляра класса:

.. code:: python

    In [1]: net1 = IPv4Network('8.8.4.0/29')

Проверка методов:

.. code:: python

    In [2]: len(net1)
    Out[2]: 6

    In [3]: net1[0]
    Out[3]: '8.8.4.1'

    In [4]: '8.8.4.1' in net1
    Out[4]: True

    In [5]: '8.8.4.10' in net1
    Out[5]: False

    In [6]: net1.count('8.8.4.1')
    Out[6]: 1

    In [7]: net1.index('8.8.4.1')
    Out[7]: 0

    In [8]: for ip in net1:
       ...:     print(ip)
       ...:
    8.8.4.1
    8.8.4.2
    8.8.4.3
    8.8.4.4
    8.8.4.5
    8.8.4.6



Задание 4.3
~~~~~~~~~~~~

Создать класс Topology, который представляет топологию сети.
Класс Topology должен наследовать абстрактный класс MutableMapping
и для всех абстрактных методов класса MutableMapping должна быть
написана рабочая реализация в классе Topology.

Проверить, что после реализации абстрактных методов, работают также
такие методы: keys, items, values, get, pop, popitem, clear, update, setdefault.

При создании экземпляра класса, как аргумент передается словарь, который описывает топологию.
В каждом экземпляре должна быть создана переменная topology, в которой
содержится словарь топологии.

Пример создания экземпляра класса:

.. code:: python

    In [1]: t1 = Topology(example1)

    In [2]: t1.topology
    Out[2]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка реализации абстрактных методов:

Получение элемента:

.. code:: python

    In [3]: t1[('R1', 'Eth0/0')]
    Out[3]: ('SW1', 'Eth0/1')


Перезапись/добавление элемента:

.. code:: python

    In [5]: t1[('R1', 'Eth0/0')] = ('SW1', 'Eth0/12')

    In [6]: t1.topology
    Out[6]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

    In [7]: t1[('R6', 'Eth0/0')] = ('SW1', 'Eth0/17')

    In [8]: t1.topology
    Out[8]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('R6', 'Eth0/0'): ('SW1', 'Eth0/17')}


Удаление:

.. code:: python

    In [11]: del t1[('R6', 'Eth0/0')]

    In [12]: t1.topology
    Out[12]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Итерация:

.. code:: python

    In [13]: for item in t1:
        ...:     print(item)
        ...:
    ('R1', 'Eth0/0')
    ('R2', 'Eth0/0')
    ('R2', 'Eth0/1')
    ('R3', 'Eth0/0')
    ('R3', 'Eth0/1')
    ('R3', 'Eth0/2')

Длина:

.. code:: python

    In [14]: len(t1)
    Out[14]: 6

После реализации абстрактных методов, должны работать таким методы:

.. code:: python

    In [1]: t1.topology
    Out[1]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

keys, values, items:

.. code:: python

    In [2]: t1.keys()
    Out[2]: KeysView(<__main__.Topology object at 0xb562f82c>)

    In [3]: t1.values()
    Out[3]: ValuesView(<__main__.Topology object at 0xb562f82c>)

Метод get:

.. code:: python

    In [4]: t1.get(('R2', 'Eth0/0'))
    Out[4]: ('SW1', 'Eth0/2')

    In [6]: print(t1.get(('R2', 'Eth0/4')))
    None

Метод pop:

.. code:: python

    In [8]: t1.pop(('R2', 'Eth0/0'))
    Out[8]: ('SW1', 'Eth0/2')

    In [9]: t1.topology
    Out[9]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Метод update:

.. code:: python

    In [10]: t2.topology
    Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

    In [11]: t1.update(t2)

    In [13]: t1.topology
    Out[13]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
     ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}


Метод clear:

.. code:: python

    In [14]: t1.clear()

    In [15]: t1.topology
    Out[15]: {}



Задание 4.3a
~~~~~~~~~~~~

Скопировать класс Topology из задания 4.3.
Переделать класс Topology таким образом, чтобы абстрактные методы
могли удалять соединение и в том случае, когда вместо ключа, передается
значение из словаря.


При создании экземпляра класса, как аргумент теперь передается словарь,
который может содержать дублирующиеся соединения.

Дублем считается ситуация, когда в словаре есть такие пары:

.. code:: python

    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1') и ('SW1', 'Eth0/1'): ('R1', 'Eth0/0')

В каждом экземпляре должна быть создана переменная topology, в которой
содержится словарь топологии, но уже без дублей. При удалении дублей
надо оставить ту пару, где key < value.

То есть ключом должно быть меньший кортеж, а значением больший.
Из таких двух пар:

.. code:: python

    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1') и ('SW1', 'Eth0/1'): ('R1', 'Eth0/0')

должна остаться первая ``('R1', 'Eth0/0'): ('SW1', 'Eth0/1')``.

Пример создания экземпляра класса:

.. code:: python

    In [1]: t1 = Topology(example1)

    In [2]: t1.topology
    Out[2]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка реализации абстрактных методов:

получение элемента:

.. code:: python

    In [3]: t1[('R1', 'Eth0/0')]
    Out[3]: ('SW1', 'Eth0/1')

    In [4]: t1[('SW1', 'Eth0/2')]
    Out[4]: ('R2', 'Eth0/0')

Перезапись/запись элемента:

.. code:: python

    In [5]: t1[('R1', 'Eth0/0')] = ('SW1', 'Eth0/12')

    In [6]: t1.topology
    Out[6]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

    In [7]: t1[('R6', 'Eth0/0')] = ('SW1', 'Eth0/17')

    In [8]: t1.topology
    Out[8]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('R6', 'Eth0/0'): ('SW1', 'Eth0/17')}

    In [9]: t1[('SW1', 'Eth0/21')] = ('R7', 'Eth0/0')

    In [10]: t1.topology
    Out[10]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('R6', 'Eth0/0'): ('SW1', 'Eth0/17'),
     ('R7', 'Eth0/0'): ('SW1', 'Eth0/21')}

Удаление:

.. code:: python

    In [11]: del t1[('R7', 'Eth0/0')]

    In [12]: t1.topology
    Out[12]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('R6', 'Eth0/0'): ('SW1', 'Eth0/17')}

    In [13]: del t1[('SW1', 'Eth0/17')]

    In [14]: t1.topology
    Out[14]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/12'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Итерация:

.. code:: python

    In [15]: for item in t1:
        ...:     print(item)
        ...:
    ('R1', 'Eth0/0')
    ('R2', 'Eth0/0')
    ('R2', 'Eth0/1')
    ('R3', 'Eth0/0')
    ('R3', 'Eth0/1')
    ('R3', 'Eth0/2')

Длина:

.. code:: python

    In [16]: len(t1)
    Out[16]: 6

Задание 4.4
~~~~~~~~~~~

Создать класс OrderingMixin, который будет автоматически добавлять к объекту методы:

* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


OrderingMixin предполагает, что в классе уже определены методы:

* __eq__ - операция ==
* __lt__ - операция <

Проверить работу примеси можно на примере класса IPAddress (класс находится в файле задания).
Определение класса можно менять.
OrderingMixin не должен использовать переменные класса IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
OrderingMixin должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.

Пример проверки методов с классом IPAddress:

.. code:: python

    In [4]: ip1 = IPAddress('10.10.1.1')

    In [5]: ip2 = IPAddress('10.2.1.1')

    In [6]: ip1 < ip2
    Out[6]: False

    In [7]: ip1 > ip2
    Out[7]: True

    In [8]: ip1 >= ip2
    Out[8]: True

    In [9]: ip1 <= ip2
    Out[9]: False

    In [10]: ip1 == ip2
    Out[10]: False

    In [11]: ip1 != ip2
    Out[11]: True


Задание 4.5
~~~~~~~~~~~

Создать примесь InheritanceMixin с двумя методами:

* subclasses - отображает дочерние классы
* superclasses - отображает родительские классы

Методы должны отрабатывать и при вызове через класс и при вызове
через экземпляр:

.. code:: python

    In [2]: A.subclasses()
    Out[2]: [__main__.B, __main__.D]

    In [3]: A.superclasses()
    Out[3]: [__main__.A, __main__.InheritanceMixin, object]

    In [4]: a.subclasses()
    Out[4]: [__main__.B, __main__.D]

    In [5]: a.superclasses()
    Out[5]: [__main__.A, __main__.InheritanceMixin, object]

В задании заготовлена иерархия классов, надо сделать так, чтобы у всех
этих классов повились методы subclasses и superclasses.
Определение классов можно менять.
