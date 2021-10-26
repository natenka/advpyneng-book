Rich Handler
------------


Настройка с logging.basicConfig:

.. code:: python

    import logging
    from rich.logging import RichHandler

    FORMAT = "%(message)s"
    logging.basicConfig(
        level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )

    log = logging.getLogger("rich")
    log.info("Hello, World!")


Настройка с Handler

.. code:: python

    from concurrent.futures import ThreadPoolExecutor
    from pprint import pprint
    from itertools import repeat
    import logging

    import yaml
    from scrapli import Scrapli
    from scrapli.exceptions import ScrapliException
    from rich.logging import RichHandler


    logging.getLogger("scrapli").setLevel(logging.WARNING)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    ### stderr
    console = RichHandler(level=logging.DEBUG)
    formatter = logging.Formatter(
        "{name} - {message}", datefmt="%X", style="{"
    )
    console.setFormatter(formatter)
    log.addHandler(console)

    ### File
    logfile = logging.FileHandler("logfile3.log")
    logfile.setLevel(logging.DEBUG)
    formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
    logfile.setFormatter(formatter)

    log.addHandler(logfile)
