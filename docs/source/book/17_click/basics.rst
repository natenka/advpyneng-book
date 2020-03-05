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

Так как для выполнения скрипта надо указать IP-адрес,
надо добавить соответствующий параметр в CLI.
Без IP-адреса скрипт запускать нет смысла, поэтому IP-адрес будут указываться
с помощью обязательного параметра - аргумента. Он также указывается декоратором.

Более практичный пример
=========================

Например, необходимо создать скрипт, который будет отправлять ICMP-запросы
на указанные IP-адрес и выводить на стандартный поток вывода информацию о том
какие адреса отвечают, а какие нет.


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

Первое, что нужно сделать, чтобы добавить CLI к этому скрипту - перенести
код из блока ``if __name__ == "__main__"`` в функцию, так как click
применяет декораторы к функции:

.. code:: python

    def main():
        ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "192.168.100.1"]
        for ip in ip_list:
            if ping_ip(ip, count=3):
                print(f"IP-адрес {ip:15} пингуется")
            else:
                print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        main()


Так как для выполнения скрипта надо указать IP-адреса и количество ICMP-запросов,
надо добавить соответствующие параметры в CLI.
Без IP-адресов скрипт запускать нет смысла, поэтому IP-адрес будут указываться
с помощью обязательного параметра - аргумента. Он также указывается декоратором.

.. code:: python

    @click.command()
    @click.argument("ip")
    def main():
        ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "192.168.100.1"]
        for ip in ip_list:
            if ping_ip(ip, count=3):
                print(f"IP-адрес {ip:15} пингуется")
            else:
                print(f"IP-адрес {ip:15} не пингуется")


    if __name__ == "__main__":
        main()


.. code:: python
.. code:: python
