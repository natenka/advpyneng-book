Опции
-----

Класс click.Option:

.. code:: python

    class click.Option(
        param_decls=None,
        show_default=False,
        prompt=False,
        confirmation_prompt=False,
        hide_input=False,
        is_flag=None,
        flag_value=None,
        multiple=False,
        count=False,
        allow_from_autoenv=True,
        type=None,
        help=None,
        hidden=False,
        show_choices=True,
        show_envvar=False,
        **attrs
    )



Имена опций:

* ``@click.option("-f", "--foo-bar")``, имя параметра функции будет ``"foo_bar"``
* ``@click.option("-x")``, имя ``"x"``
* ``@click.option("-f", "--filename", "dest")``, имя ``"dest"``
* ``@click.option("--CamelCase")``, имя ``"camelcase"``
* ``@click.option("-f", "-fb")``, имя ``"f"``
* ``@click.option("--f", "--foo-bar")``, имя ``"f"``
* ``@click.option("---f")``, имя ``"_f"``

Запрос значения у пользователя
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Запрос выполняется только если в опции не указано значение:

.. code:: python

    @click.command()
    @click.option("--username", "-u", prompt=True)
    @click.option("--password", "-p", prompt=True, hide_input=True)
    @click.option("--secret", "-s", prompt=True, hide_input=True)
    def cli(username, password, secret):
        pass

Параметр hide_input позволяет скрывать вводимое значение.

Переменные окружения
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    @click.command()
    @click.option("--username", "-u", envvar="NET_USER")
    @click.option("--password", "-p", envvar="NET_PASSWORD")
    @click.option("--secret", "-s", envvar="NET_SECRET")
    def cli(username, password, secret):
        pass

Переменные окружения и prompt - сначала проверяется переменная окружения, потом, если ее нет,
запрос у пользователя:

.. code:: python

    @click.command()
    @click.option("--username", "-u", envvar="NET_USER", prompt=True)
    @click.option("--password", "-p", envvar="NET_PASSWORD", prompt=True, hide_input=True)
    @click.option("--secret", "-s", envvar="NET_SECRET", prompt=True, hide_input=True)
    def cli(username, password, secret):
        pass

Флаг
~~~~

.. code:: python

    @click.option("--show-all", "-a", is_flag=True, help="show db content")


