Аргументы
---------

Аргументы создаются с помощью декоратора ``@click.argument``:

.. code:: python

    @click.argument(name, type=None, required=True, default=None, nargs=None)


В самом простом случае, достаточно указать только имя аргумента:

.. code:: python

    @click.command()
    @click.argument("name")
    def cli(name):
        """Print NAME"""
        print(name)

Так будет выглядеть help скрипта:

::

    $ python basics_01.py --help
    Usage: basics_01.py [OPTIONS] NAME

      Print NAME

    Options:
      --help  Show this message and exit.


И так вызов:

::

    $ python basics_01.py R2D2
    R2D2

Переменное количество аргументов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Параметр nargs позволяет контролировать какое количество аргументов можно передать.
По умолчанию, значение 1. Значение -1 - это специальное значение обозначающее, что аргументов может быть
сколько угодно.

Пример использования nargs

.. code:: python

    import subprocess
    import click


    def ping_ip(ip_address):
        reply = subprocess.run(
            f"ping -c 2 -n {ip_address}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        if reply.returncode == 0:
            return True
        else:
            return False


    @click.command()
    @click.argument("ip_addresses", nargs=-1, required=True)
    def cli(ip_addresses):
        """
        Ping IP_ADDRESSES
        """
        for ip in ip_addresses:
            if ping_ip(ip):
                print(f"IP-адрес {ip:15} пингуется")
            else:
                print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        cli()

