Дополнительные возможности
--------------------------


* ``click.password_option(*param_decls, **attrs)``
* ``click.confirmation_option(*param_decls, **attrs)``
* ``click.version_option(version=None, *param_decls, **attrs)``
* click.echo
* click.style
* click.secho
* click.clear
* click.pause
* click.prompt
* click.confirm
* click.echo_via_pager
* click.progressbar


Декоратор click.password_option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Декоратор click.password_option равнозначен такой опции:

.. code:: python

    @click.option("--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True)

Пример использования:

.. code:: python

    @click.command()
    @click.option("--username", "-u", prompt=True)
    @click.password_option()
    def cli(username, password):
        print(username, password)

click.echo, click.style, click.secho
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция click.echo в целом работает как print, но при этом:

* добавляет обработку цветовых кодов ANSI в Windows
* автоматически скрывает коды ANSI, если вывод идет не в терминал

click.style добавляет возможность выводить текст в цвете. Использовать можно или так

.. code:: python

    click.echo(click.style('Hello World!', fg='green'))

Или использовать короткий вариант click.secho:

.. code:: python

    click.secho('Hello World!', fg='green')

click.progressbar
~~~~~~~~~~~~~~~~~


.. code:: python

    def ping_ip_addresses(ip_addresses, count):
        reachable = []
        unreachable = []
        with click.progressbar(ip_addresses, label="Пингую адреса") as bar:
            for ip in bar:
                if ping_ip(ip, count):
                    reachable.append(ip)
                else:
                    unreachable.append(ip)
        return reachable, unreachable

Вывод:

::

    $ python example_03_ping_ip_list_progress_bar.py 8.8.8.8 8.8.4.4 10.1.1.1 192.168.100.1
    Пингую адреса  [####################################]  100%
    IP-адрес 8.8.8.8         пингуется
    IP-адрес 8.8.4.4         пингуется
    IP-адрес 192.168.100.1   пингуется
    IP-адрес 10.1.1.1        не пингуется


.. code:: python

    def send_command_to_devices(devices, command, limit):
        results = []
        with ThreadPoolExecutor(max_workers=limit) as executor:
            futures = [
                executor.submit(send_show_command, device, command) for device in devices
            ]
            with click.progressbar(
                length=len(futures), label="Connecting to devices"
            ) as bar:
                for future in as_completed(futures):
                    results.append(future.result())
                    bar.update(1)
        return results

click.clear
~~~~~~~~~~~

Функция click.clear очищает экран. Удобно выполнять в начале работы скрипта.

.. code:: python

    def cli(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
        click.clear()
        all_pomodoros = list(range(1, pomodoros_to_run + 1))
        pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
        for pomo_set in pomodoro_sets:
            run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)


click.pause
~~~~~~~~~~~

Функция click.pause останавливает выполнение скрипта, выводит сообщение
"Press any key to continue ..." и ждет нажатия любой клавиши. Использовать можно в любом месте,
таким образом

.. code:: python
    
    click.pause()
