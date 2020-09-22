Другие декораторы
-----------------

* ``click.password_option(*param_decls, **attrs)``
* ``click.confirmation_option(*param_decls, **attrs)``
* ``click.version_option(version=None, *param_decls, **attrs)``


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
