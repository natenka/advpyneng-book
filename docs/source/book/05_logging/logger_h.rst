Иерархия логеров
----------------

В модуле logging есть иерархия логеров. Самый главный в иерархии root. 
Остальные под ним, часто, на одном уровне. В одном модуле может быть много логеров с разной иерархией,
например, в paramiko есть логер paramiko.transport, он по иерархии ниже paramiko.

Такой конфиг настраивает logger root:

.. code:: python

    logging.basicConfig(
        level=logging.INFO
    )

Так как он самый главный, его настройка приводит к тому, что все остальные логеры тоже начинают отображать информацию.
При такой настройке настраивается конкретный logger и никакие другие логи уже не сыпятся.

.. code:: python

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(threadName)s %(name)s %(levelname)s %(asctime)s: %(message)s", datefmt="%H:%M:%S"
    )
    console.setFormatter(formatter)
    logger.addHandler(console)


Хотя тут тоже можно использовать root, для этого надо первую строку написать так

.. code:: python
    logger = logging.getLogger()

С базовым конфигом надо отключить или хотя бы приглушить на какой-то уровень существующие логеры других модулей:

.. code:: python

    logging.getLogger("paramiko").setLevel(logging.WARNING)

    logging.basicConfig(
        level=logging.INFO
    )

Со своим логером (не root) - надо наоборот добавить строк чтобы включить logger netmiko/paramiko.
Для этого надо добавлять такие строки (учитывая что предыдущие все есть с handler, formatter И тп

.. code:: python

    netmiko_log = logging.getLogger("netmiko")
    netmiko_log.setLevel(logging.DEBUG)
    netmiko_log.addHandler(console)

