Основы click
------------

Терминология:

* параметры
* аргументы
* опции

В click описание интерфейса командной строки (CLI) построено на декораторах:

* аргументы создаются с помощью декоратора click.argument
* опции с помощью декоратора click.option


Пример скрипта, который пингует только один IP-адрес (ping_ip.py):

.. code:: python

    import subprocess


    def ping_ip(ip_address, count):
        """
        Ping IP address and return True/False
        """
        reply = subprocess.run(
            f"ping -c {count} -n {ip_address}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if reply.returncode == 0:
            return True
        else:
            return False


    if __name__ == "__main__":
        ip = "8.8.8.8"
        if ping_ip(ip, count=3):
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")


Первое, что нужно сделать, чтобы добавить CLI к этому скрипту - перенести
код из блока ``if __name__ == "__main__"`` в функцию, так как click
применяет декораторы к функции:

.. code:: python

    def main():
        ip = "8.8.8.8"
        if ping_ip(ip, count=3):
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        main()

Следующий шаг - превратить функцию main в команду click. Для этого надо применить 
декоратор click.command и импортировать click:

.. code:: python

    import click

    @click.command()
    def main():
        ip = "8.8.8.8"
        if ping_ip(ip, count=3):
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        main()

Теперь вызов скрипта отработает так же, но у скрипта появилась опция --help:

::

    $ python ping_ip_click.py --help
    Usage: ping_ip_click.py [OPTIONS]

    Options:
      --help  Show this message and exit.

Так как для выполнения скрипта надо указать IP-адрес, надо добавить соответствующий параметр в CLI.
Без IP-адреса скрипт запускать нет смысла, поэтому IP-адрес будут указываться
с помощью обязательного параметра - аргумента. Он также указывается декоратором:

.. code:: python

    @click.command()
    @click.argument("ip_address")
    def main(ip_address):
        if ping_ip(ip_address, count=3):
            print(f"IP-адрес {ip_address:15} пингуется")
        else:
            print(f"IP-адрес {ip_address:15} не пингуется")


    if __name__ == "__main__":
        main()

Строка ``@click.argument("ip_address")`` указывает, что теперь скрипт ожидает один
обязательный параметр - ip_address, а также функция main должна принимать аргумент с таким именем,
так как click автоматически передаст значение, которое передается при вызове скрипта,
как ключевой аргумент функции, используя имя аргумента.

Теперь опция --help отображает такой вывод:

::

    $ python ping_ip_click.py --help
    Usage: ping_ip_click.py [OPTIONS] IP_ADDRESS

    Options:
      --help  Show this message and exit.

И при вызове скрипта обязательно надо передать IP-адрес:

::

    $ python ping_ip_click.py
    Usage: ping_ip_click.py [OPTIONS] IP_ADDRESS
    Try "ping_ip_click.py --help" for help.

    Error: Missing argument "IP_ADDRESS".


    $ python ping_ip_click.py 8.8.8.8
    IP-адрес 8.8.8.8         пингуется

Так как функция зависит от еще одного значения - count, надо добавить еще один параметр click,
в этот раз - опцию. Опции создаются с помощью декоратора click.option:

.. code:: python

    @click.command()
    @click.argument("ip_address")
    @click.option("--count", "-c", default=3)
    def main(ip_address, count):
        if ping_ip(ip_address, count):
            print(f"IP-адрес {ip_address:15} пингуется")
        else:
            print(f"IP-адрес {ip_address:15} не пингуется")


    if __name__ == "__main__":
        main()

Так же как с аргументом, click будет передавать как ключевой аргумент имя опции и значение,
которое было указано при вызове скрипта. Так как в данном случае у опции есть значение по
умолчанию, если опция не указана передается значение 3.
Еще одно следствие задания значения по умолчанию - click теперь считает, что count обязательно
должен быть числом. Это поведение можно менять, указав тип параметра явно, но в данном случае,
он подходит.

Запуск скрипта с вводом данных неправильного типа:

::

    $ python ping_ip_click.py 8.8.8.8
    IP-адрес 8.8.8.8         пингуется


    $ python ping_ip_click.py 8.8.8.8 -c a
    Usage: ping_ip_click.py [OPTIONS] IP_ADDRESS
    Try "ping_ip_click.py --help" for help.

    Error: Invalid value for "--count" / "-c": a is not a valid integer


    $ python ping_ip_click.py 8.8.8.8 -c 1
    IP-адрес 8.8.8.8         пингуется

И help для текущей версии скрипта:

::

    $ python ping_ip_click.py --help
    Usage: ping_ip_click.py [OPTIONS] IP_ADDRESS

    Options:
      -c, --count INTEGER
      --help               Show this message and exit.


По умолчанию click не отображает значение, которое указано в default.
Если необходимо это изменить, надо добавить в настройку опции ``show_default=True``:

::

    $ python ping_ip_click.py --help
    Usage: ping_ip_click.py [OPTIONS] IP_ADDRESS

    Options:
      -c, --count INTEGER  [default: 3]
      --help               Show this message and exit.


Более практичный пример
=======================

Предыдущий пример использовался для демонстрации базовых настроек click и на практике
не очень полезен. Чтобы сделать скрипт более интересным, можно добавить возможность
отправлять ICMP-запросы на несколько IP-адресов и выводить на стандартный поток вывода
информацию о том какие адреса отвечают, а какие нет.


Пример скрипта без использования click:

.. code:: python

    import subprocess


    def ping_ip(ip_address, count):
        """
        Ping IP address and return True/False
        """
        reply = subprocess.run(
            f"ping -c {count} -n {ip_address}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if reply.returncode == 0:
            return True
        else:
            return False


    if __name__ == "__main__":
        ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "192.168.100.1"]
        for ip in ip_list:
            if ping_ip(ip, count=3):
                print(f"IP-адрес {ip:15} пингуется")
            else:
                print(f"IP-адрес {ip:15} не пингуется")

Пример выполнения скрипта

::

    $ python ping_ip_list.py
    IP-адрес 8.8.8.8         пингуется
    IP-адрес 8.8.4.4         пингуется
    IP-адрес 10.1.1.1        не пингуется
    IP-адрес 192.168.100.1   пингуется

Этот скрипт отличается от предыдущего тем, что теперь аргументу передается
не один IP-адрес, а несколько. Click поддерживает такую возможность с помощью
указания nargs в настройках аргумента.
Так как в данном случае количество IP-адресов точно не известно, надо сделать так
чтобы аргумент мог принимать любое количество. Для этого надо указать ``nargs=-1``
и, так как надо передать хотя бы один адрес, дополнительно указать ``required=True``:

.. code:: python

    @click.command()
    @click.argument("ip_address", nargs=-1, required=True)
    @click.option("--count", "-c", default=3)
    def main(ip_address, count):
        for ip in ip_address:
            if ping_ip(ip, count=3):
                print(f"IP-адрес {ip:15} пингуется")
            else:
                print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        main()

Опция --help выглядит так:

::

    $ python ping_ip_list_click.py --help
    Usage: ping_ip_list_click.py [OPTIONS] IP_ADDRESS...

    Options:
      -c, --count INTEGER
      --help               Show this message and exit.


И вызывать скрипт теперь можно таким образом:

::

    $ python ping_ip_list_click.py 8.8.8.8 10.1.1.1 8.8.4.4 192.168.100.1
    IP-адрес 8.8.8.8         пингуется
    IP-адрес 10.1.1.1        не пингуется
    IP-адрес 8.8.4.4         пингуется
    IP-адрес 192.168.100.1   пингуется

    $ python ping_ip_list_click.py 8.8.8.8 10.1.1.1 8.8.4.4 192.168.100.1 -c 2
    IP-адрес 8.8.8.8         пингуется
    IP-адрес 10.1.1.1        не пингуется
    IP-адрес 8.8.4.4         пингуется
    IP-адрес 192.168.100.1   пингуется

Перечисленные IP-адреса попадают в функцию в виде кортежа со строками.
