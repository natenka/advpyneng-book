
.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst

Задание 6.1
~~~~~~~~~~~

Переделать функцию netmiko_ssh таким образом, чтобы при отправке строки "close",
вместо отправки "close" как команды на оборудование, закрывалось соединение к устройству
и выводилось сообщение 'Соединение закрыто'.

Пример работы функции:

.. code:: python

    In [1]: r1 = netmiko_ssh(**device_params)

    In [2]: r1('sh clock')
    Out[2]: '*08:07:44.267 UTC Thu Oct 17 2019'

    In [3]: r1('close')
    Соединение закрыто

Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.

.. code:: python

    from netmiko import ConnectHandler

    device_params = {
        'device_type': 'cisco_ios',
        'ip': '192.168.100.1',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'
    }


    def netmiko_ssh(**params_dict):
        ssh = ConnectHandler(**params_dict)
        ssh.enable()
        def send_show_command(command):
            return ssh.send_command(command)
        return send_show_command


    if __name__ == "__main__":
        r1 = netmiko_ssh(**device_params)
        print(r1('sh clock'))

Задание 6.2
~~~~~~~~~~~

Создать функцию count_total, которая вычисляет сумму потраченную на категорию товаров.
После вызова функции count_total, должна возвращаться внутренняя функция.
При вызове внутренней функции надо передавать аргумент - число.
Как результат должна возвращаться текущая сумма чисел.

Пример использования функции count_total:

.. code:: python

    In [2]: books = count_total()

    In [3]: books(25)
    Out[3]: 25

    In [4]: books(15)
    Out[4]: 40

    In [5]: books(115)
    Out[5]: 155

    In [6]: books(25)
    Out[6]: 180

    In [7]: toys = count_total()

    In [8]: toys(67)
    Out[8]: 67

    In [9]: toys(17)
    Out[9]: 84

    In [10]: toys(24)
    Out[10]: 108

Задание 6.2a
~~~~~~~~~~~~

Изменить функцию count_total из задания 6.2a.
После вызова функции count_total, должна быть доступна возможность обращаться к
атрибуту buy и передавать ему аргумент - число. Как результат должна возвращаться
текущая сумма чисел.

Пример использования функции count_total:

.. code:: python

    In [2]: books = count_total()

    In [3]: books.buy(25)
    Out[3]: 25

    In [4]: books.buy(15)
    Out[4]: 40

    In [5]: books.buy(115)
    Out[5]: 155

    In [6]: books.buy(25)
    Out[6]: 180

    In [7]: toys = count_total()

    In [8]: toys.buy(67)
    Out[8]: 67

    In [9]: toys.buy(17)
    Out[9]: 84

    In [10]: toys.buy(24)
    Out[10]: 108


Задание 6.3
~~~~~~~~~~~

Создать функцию queue, которая работает как очередь.
После вызова функции queue, должна быть доступна возможность обращаться к
атрибутам:

* put - добавляет элемент в очередь
* get - удаляет элемент с начала очереди и возвращает None, если элементы закончились

Пример работы функции queue:

.. code:: python

    In [2]: tasks = queue()

    In [3]: tasks.put('a')

    In [4]: tasks.put('b')

    In [5]: tasks.put('c')

    In [6]: tasks.get()
    Out[6]: 'a'

    In [7]: tasks.get()
    Out[7]: 'b'

    In [8]: tasks.get()
    Out[8]: 'c'

    In [9]: tasks.get()

    In [10]: tasks.get()

