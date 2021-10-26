Фильтры
--------

Фильтры можно применять к logger или к handler

.. note::

    `LogRecord attributes <https://docs.python.org/3.10/library/logging.html#logrecord-attributes>`__

.. code:: python

    class LevelFilter(logging.Filter):
        def __init__(self, level):
            self.level = level

        def filter(self, record):
            return record.levelno == self.level


    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addFilter(LevelFilter(logging.DEBUG))

    logfile = logging.FileHandler("logfile3.log")
    logfile.setLevel(logging.DEBUG)
    formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
    logfile.setFormatter(formatter)

    log.addHandler(logfile)


Handler Filter
~~~~~~~~~~~~~~

.. code:: python

    class LevelFilter(logging.Filter):
        def __init__(self, level):
            self.level = level

        def filter(self, record):
            return record.levelno == self.level


    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    logfile = logging.FileHandler("logfile3.log")
    logfile.setLevel(logging.DEBUG)
    logfile.addFilter(LevelFilter(logging.DEBUG))
    logfile.addFilter(MessageFilter("test"))

    formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
    logfile.setFormatter(formatter)

    log.addHandler(logfile)


Использование фильтра для добавления информации в запись
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    `Using Filters to impart contextual information <https://docs.python.org/3/howto/logging-cookbook.html#using-filters-to-impart-contextual-information>`__


.. code:: python

    class AddIPFilter(logging.Filter):
        def filter(self, record):
            match = re.search(r"\d+\.\d+\.\d+\.\d+", record.msg)
            if match:
                record.ip = match.group()
            else:
                record.ip = None
            return True

