Установка скрипта через setuptools
----------------------------------

.. seealso::

    `Интеграция click с setuptools <https://click.palletsprojects.com/en/7.x/setuptools/>`__

Скрипты с интерфейсом командной строки можно запускать с указанием `shebang и сделав скрипт исполняемым <https://pyneng.readthedocs.io/ru/latest/book/05_basic_scripts/0_executable.html>`__
или использовать setuptools.

Setuptools - это набор утилит для работы с пакетами Python. В нем есть масса
возможностей, тут рассматривается лишь базовые пример. `Подробнее в документации <https://setuptools.readthedocs.io/en/latest/index.html>`__

Преимущества использования setuptools:

* запуск будет работать на Linux/Windows одинаково
* setuptools умеет работать с Python package


Пример базового использования setuptools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Пример использования setuptools для скрипта example_05_pomodoro_timer.py.

Скрипт example_05_pomodoro_timer.py (вывод сокращен):

.. code:: python

    from datetime import datetime, date, timedelta
    import time
    import sys

    import click

    # ...

    @click.command()
    @click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
    @click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
    @click.option("--short_break", "-s", default=5, show_default=True, type=int)
    @click.option("--long_break", "-l", default=30, show_default=True, type=int)
    @click.option("--set_size", "-p", default=4, show_default=True, type=int)
    def cli(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
        session_stats = {"total": pomodoros_to_run, "done": 0, "todo": pomodoros_to_run}
        global stats
        stats = update_session_stats(session_stats)

        click.clear()
        all_pomodoros = list(range(1, pomodoros_to_run + 1))
        pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
        for pomo_set in pomodoro_sets:
            run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)


    if __name__ == "__main__":
        cli()


Файл setup.py

.. code:: python

    from setuptools import setup

    setup(
        name='pomodoro',
        version='1.0',
        py_modules=['example_05_pomodoro_timer'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            pomodoro=example_05_pomodoro_timer:cli
        ''',
    )


Это очень базовый пример файла setup.py, но для своих скриптов его может быть вполне достаточно.
Параметры setup:

* ``name='pomodoro'`` - это имя приложения/скрипта
* ``version='1.0'`` - версия скрипта
* ``py_modules=['example_05_pomodoro_timer']`` - основной скрипт, который надо запускать
* ``install_requires=['Click']`` - зависимости скрипта

И последний параметр ``entry_points``:

.. code:: python

        entry_points='''
            [console_scripts]
            pomodoro=example_05_pomodoro_timer:cli
        '''

* первое слово pomodoro - это команда, которая вызывает скрипт,
* example_05_pomodoro_timer - какой скрипт запустить (то же самое, что в py_modules)
* cli - в нашем случае это имя функции к которой привязана настройка click


Установка скрипта после создания setup.py (тут есть много вариантов, в часности запуск установки в development режиме -e):

::

    $ pip install .
    Processing /home/vagrant/repos/advanced-pyneng-2/advpyneng-online-2-sep-nov-2020/examples/03_click
    Requirement already satisfied: Click in /home/vagrant/venv/pyneng-py3-8-0/lib/python3.8/site-packages (from pomodoro==1.0) (7.1.2)
    Building wheels for collected packages: pomodoro
      Building wheel for pomodoro (setup.py) ... done
      Created wheel for pomodoro: filename=pomodoro-1.0-py3-none-any.whl size=2416 sha256=15a4751c3e03ab7da4f5e2ee979f54fadcc4a1724ce8f6994ee5966c3c8af193
      Stored in directory: /tmp/pip-ephem-wheel-cache-n_s8xn0d/wheels/b3/ff/4f/e229093f911f6ad2ba16bbb55fbc28dd4cf701f7fe60d9333a
    Successfully built pomodoro
    Installing collected packages: pomodoro
    Successfully installed pomodoro-1.0

После этого скрипт можно вызывать по pomodoro в любом месте:

::

    [~/repos/advanced-pyneng-2/advpyneng-online-2-sep-nov-2020]
    $ pomodoro
    It's time to work!
    Pomodoro 1
    Work: 0:00:01^C
    Aborted!

Удалить скрипт:

::

    $ pip uninstall pomodoro
    Found existing installation: pomodoro 1.0
    Uninstalling pomodoro-1.0:
      Would remove:
        /home/vagrant/venv/pyneng-py3-8-0/bin/pomodoro
        /home/vagrant/venv/pyneng-py3-8-0/lib/python3.8/site-packages/example_05_pomodoro_timer.py
        /home/vagrant/venv/pyneng-py3-8-0/lib/python3.8/site-packages/pomodoro-1.0.dist-info/*
    Proceed (y/n)? y
      Successfully uninstalled pomodoro-1.0

