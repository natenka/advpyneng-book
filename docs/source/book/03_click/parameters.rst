Параметры
---------

Click поддерживает два вида параметров: опции и аргументы. В click аргументы имеют больше ограничений.

Возможности доступные только в опциях:

* запрос ввода значения опции у пользователя
* опции могут использоваться как флаги
* значения опций можно считывать из переменных окружения м автоматическим префиксом
* опциям можно писать help

Возможности доступные только в аргументах:

* передача любого количества значений


Типы параметров
~~~~~~~~~~~~~~~

По умолчанию тип параметра будет строкой str, но его можно задавать явно
или получать косвенно с помощью значения по умолчанию.

Доступные типы (большинство типов показаны в примерах опций):

* базовые типы: str, int, float, bool
* click.File - специальный тип, который автоматически открывает и закрывает файл. Возвращает открытый файл
* click.Path - тип для проверки пути, файл это или каталог и подобного. Возвращает строку, не открытый файл
* click.Choice - набор допустимых значений
* click.IntRange - диапазон числовых значений
* click.DateTime - преобразует строку с датой в объект datetime


.. note::

    `Также можно создавать свои типы данных <https://click.palletsprojects.com/en/7.x/parameters/#implementing-custom-types>`__

Базовые типы: str, int, float, bool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Если указать, что тип параметра int или float, click будет проверять, что скрипту 
как аргумент передается именно этот тип данных. Например:


.. code:: python

    @click.command()
    @click.argument("ip_address")
    @click.option("--count", "-c", type=int, help="Number of packets")
    def main(ip_address, count):
        pass

При вызове скрипта, опция ``-c`` ожидает значение типа int:

::

    $ python example_03_ping_ip_list_progress_bar.py 8.8.8.8 -c test
    Usage: example_03_ping_ip_list_progress_bar.py [OPTIONS] IP_ADDRESS
    Try 'example_03_ping_ip_list_progress_bar.py --help' for help.

    Error: Invalid value for '--count' / '-c': test is not a valid integer


click.File
^^^^^^^^^^

Тип click.File

.. code:: python

    class click.File(mode='r', encoding=None, errors='strict', lazy=None, atomic=False)


Этот тип используется для работы с файлами. Особенность типа clicl.File в том, что файл 
автоматически открывается и закрывается click. Файл может быть открыт для чтения или записи,
плюс специальное значение ``-`` указывает, что вместо файла надо открыть stdin/stdout.

Пример аргумента с типом click.File:

.. code:: python

    @click.command()
    @click.argument("connection_params", type=click.File("r"))
    def cli(connection_params):
        devices = yaml.safe_load(connection_params)


Так как click открывает файл, внутри функции cli connection_params это уже открытый файл.


click.Choice
^^^^^^^^^^^^

Тип click.Choice позволяет указать допустимые варианты значений для параметра:

.. code:: python

    @click.command()
    @click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
    def cli(key):
        pass

Если при вызове скрипта передать другое значение, возникнет ошибка:

::

    $ python example_choice.py --key test
    ...
    Error: Invalid value for '--key' / '-k': invalid choice: test. (choose from mac, ip, vlan)


click.IntRange
^^^^^^^^^^^^^^

Тип click.IntRange:

.. code:: python

    class click.IntRange(min=None, max=None, clamp=False)

Пример использования:

.. code:: python

    @click.command()
    @click.option("--threads", "-t", type=click.IntRange(1, 10))
    def cli(threads):
        pass

Если указанное значение не попадает в диапазон, по умолчанию возникнет ошибка.
Если установить ``clamp=True``, вместо ошибки, значение будет подгоняться под ближайшую границу.
Например, если в примере выше передать 20, то threads будет равен 10.

