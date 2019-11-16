Базовый пример
--------------

logging_basic_1.py

.. code:: python

    import logging

    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)

    logging.debug('Сообщение уровня debug')
    logging.info('Сообщение уровня info')
    logging.warning('Сообщение уровня warning')

Log-файл

::
    DEBUG:root:Сообщение уровня debug
    INFO:root:Сообщение уровня info
    WARNING:root:Сообщение уровня warning

logging_basic_2.py

.. code:: python


    import logging

    logging.basicConfig(filename='mylog2.log', level=logging.DEBUG)

    logging.debug('Сообщение уровня debug:\n%s', str(globals()))
    logging.info('Сообщение уровня info')
    logging.warning('Сообщение уровня warning')


Log-файл

::

    DEBUG:root:Сообщение уровня debug:
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0xb72a57ac>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'logging_basic_2.py', '__cached__': None, 'logging': <module 'logging' from '/usr/local/lib/python3.6/logging/__init__.py'>}
    INFO:root:Сообщение уровня info
    WARNING:root:Сообщение уровня warning



Рекомендации
------------

https://gitpitch.com/pitchme/cdn/github/natenka/pyneng-slides/bonus-logging/6B32347FFCECBC648621A3C3974C7E85EFC4AFEFC87CD001646A84FD62209FC093F8F7EC317FE1ABD3A2DD0CBC40EAC15F7E66DE705A685554EC65C15A0FC410764746F2CF5250C0204669103B3CA395B60FFC52D19258D66546CDA4128FCC0F342D66D186B12616/assets/when_to_use_logging.png

Уровни

https://gitpitch.com/pitchme/cdn/github/natenka/pyneng-slides/bonus-logging/6B32347FFCECBC648621A3C3974C7E85EFC4AFEFC87CD001646A84FD62209FC093F8F7EC317FE1ABD3A2DD0CBC40EAC15F7E66DE705A685554EC65C15A0FC410764746F2CF5250C0204669103B3CA395B60FFC52D19258D66546CDA4128FCC0F342D66D186B12616/assets/log_levels.png


