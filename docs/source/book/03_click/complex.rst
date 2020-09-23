Большие приложения
------------------

Для более сложных приложений, интерфейс командной строки, как правило, тоже
усложняется. С помощью Click можно создавать сложные интерфейсы командной строки,
но для этого надо разобраться с понятием контекста.

Контекст (Context) это внутренний объект Click, который создается при выполнении команды
click и содержит информацию о том какая команда была вызвана, с какими параметрами. 
В простых случаях с контекстом не нужно работать напрямую, но можно посмотреть на него,
если добавить декоратор ``click.pass_context`` к функции:

.. code:: python

    import click


    @click.command()
    @click.argument("ip_address")
    @click.option("--count", "-c", default=2, type=int, help="Number of packets")
    @click.pass_context
    def ping_ip(ctx, ip_address, count):
        """
        Ping IP address and return True/False
        """
        print(ctx.command)
        print(ctx.params)


    if __name__ == "__main__":
        ping_ip()

Вывод будет таким:

::

    $ python example_01_ping_function.py 8.8.8.8
    <Command ping-ip>
    {'ip_address': '8.8.8.8', 'count': 2}

В выводе видно какая команда была вызвана - ping-ip и какие параметры были указаны:
тут и значение адреса 8.8.8.8 и значение опции по умолчанию - 2.

Кроме того, что контекст содержит много информации для самого click, ему можно присваивать 
произвольные значение в атрибут obj. Этот атрибут используется для передачи информации
между группой команд и командами. Когда значений несколько, как правило, используется словарь.

click.group
~~~~~~~~~~~

click.group это декоратор, который работает так же как click.command, но при этом позволяет создавать 
подкоманды. Пример интерфейса с подкомандами - git. В зависимости от того какая команда пишется после git,
появляются разные аргументы и опции.

Пример интерфейса с группой:

.. code:: python

    import click


    @click.group()
    def pomodoro_cli():
        pass


    @pomodoro_cli.command()
    @click.option("--day", "-d", is_flag=True)
    @click.option("--week", "-w", is_flag=True)
    @click.option("--month", "-m", is_flag=True)
    def stats(day, week, month):
        print("STATS")


    @pomodoro_cli.command()
    @click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
    @click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
    @click.option("--short_break", "-s", default=5, show_default=True, type=int)
    @click.option("--long_break", "-l", default=30, show_default=True, type=int)
    @click.option("--set_size", "-p", default=4, show_default=True, type=int)
    def work(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
        pass


    if __name__ == "__main__":
        pomodoro_cli()

Первой надо создать функцию, которая является группой, так как затем имя функции
используется в декораторах других функций, вместо click:

.. code:: python

    @click.group()
    def pomodoro_cli():
        pass

Следующие две функции создают подкоманды скрипта stats и work (как commit и add в git). Имена функций
будут именами команд. У этих функций могут быть свои аргументы и опции.
Единственное отличие от предыдущих примеров - это то, что вместо декоратора ``click.command`` используется
``pomodoro_cli.command``. Таким образом указывается, что команда относится к группе pomodoro_cli:

.. code:: python

    @pomodoro_cli.command()
    @click.option("--day", "-d", is_flag=True)
    @click.option("--week", "-w", is_flag=True)
    @click.option("--month", "-m", is_flag=True)
    def stats(day, week, month):
        print("STATS")


    @pomodoro_cli.command()
    @click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
    @click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
    @click.option("--short_break", "-s", default=5, show_default=True, type=int)
    @click.option("--long_break", "-l", default=30, show_default=True, type=int)
    @click.option("--set_size", "-p", default=4, show_default=True, type=int)
    def work(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
        pass

При такой настройке help скрипта выглядит таким образом:

::

    $ python example_11_click_group_basics.py --help
    Usage: example_11_click_group_basics.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      stats
      work

У каждой команды есть свой help:

::

    $ python example_11_click_group_basics.py stats --help
    Usage: example_11_click_group_basics.py stats [OPTIONS]

    Options:
      -d, --day
      -w, --week
      -m, --month
      --help       Show this message and exit.


    $ python example_11_click_group_basics.py work --help
    Usage: example_11_click_group_basics.py work [OPTIONS]

    Options:
      -r, --pomodoros_to_run INTEGER  [default: 5]
      -w, --work_minutes INTEGER      [default: 25]
      -s, --short_break INTEGER       [default: 5]
      -l, --long_break INTEGER        [default: 30]
      -p, --set_size INTEGER          [default: 4]
      --help                          Show this message and exit.

В этом случае у каждой команды свои параметры, плюс команд мало.
Часто бывают случаи, когда часть параметров команд пересекаются и, особенно
если команд много, их становится неудобно описывать, так как параметры приходится повторять.

Тут на помощь приходит контекст.

click.pass_context
~~~~~~~~~~~~~~~~~~


