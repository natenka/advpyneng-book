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

* ``"-f"``, ``"--foo-bar"``, имя параметра функции будет ``"foo_bar"``
* ``"-x"``, имя ``"x"``
* ``"-f"``, ``"--filename"``, ``"dest"``, имя ``"dest"``
* ``"--CamelCase"``, имя ``"camelcase"``
* ``"-f"``, ``"-fb"``, имя ``"f"``
* ``"--f"``, ``"--foo-bar"``, имя ``"f"``
* ``"---f"``, имя ``"_f"``

