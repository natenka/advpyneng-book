
.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst

Задание 7.1
~~~~~~~~~~~

Создать декоратор timecode, который засекает время выполнения декорируемой функции
и выводит время на стандартный поток вывода. Декоратор должен работать с любой функцией.

Проверить работу декоратора на функции send_show_command.

Пример вывода:

.. code:: python

    In [3]: @timecode
       ...: def send_show_command(params, command):
       ...:     with ConnectHandler(**params) as ssh:
       ...:         ssh.enable()
       ...:         result = ssh.send_command(command)
       ...:     return result
       ...:

    In [4]: print(send_show_command(device_params, 'sh clock'))
    >>> Функция выполнялась: 0:00:05.527703
    *13:02:49.080 UTC Mon Feb 26 2018


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


    def send_show_command(params, command):
        with ConnectHandler(**params) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result


    if __name__ == "__main__":
        print(send_show_command(device_params, 'sh clock'))


Задание 7.2
~~~~~~~~~~~

Переделать декоратор all_args_str таким образом, чтобы он проверял
не только позиционные аргументы, но и ключевые тоже.

.. code:: python

    In [2]: concat_str(str1='b', str2='a')
    Out[2]: 'ba'

    In [3]: concat_str(str1='b', str2=1)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-3-08af972add0a> in <module>
    ----> 1 concat_str(str1='b', str2=1)
    ...
    ValueError: Все аргументы должны быть строками


    In [4]: concat_str('b', 1)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-4-864f6fda8c8b> in <module>
    ----> 1 concat_str('b', 1)
    ...
    ValueError: Все аргументы должны быть строками


Задание 7.3
~~~~~~~~~~~

Создать декоратор add_verbose, который добавляет в функцию
дополнительный параметр verbose.
Когда параметру передано значение True, на стандартный поток вывода
должна отображаться информация о вызове функции и ее аргументах
(пример работы декоратора показан ниже).

По умолчанию, значение параметра должно быть равным False.

Проверить работу декоратора на функции send_show_command.

Пример вывода:

.. code:: python

    In [3]: @add_verbose
       ...: def send_show_command(params, command):
       ...:     with ConnectHandler(**params) as ssh:
       ...:         ssh.enable()
       ...:         result = ssh.send_command(command)
       ...:     return result
       ...:

    In [4]: print(send_show_command(device_params, 'sh clock', verbose=True))
    Вызываем send_show_command
    Позиционные аргументы: ({'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'sh clock')
    *14:01:07.353 UTC Mon Feb 26 2018

    In [5]: print(send_show_command(device_params, 'sh clock', verbose=True))
    Вызываем send_show_command
    Позиционные аргументы: ({'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'sh clock')
    *15:09:45.152 UTC Fri Oct 18 2019

    In [6]: print(send_show_command(device_params, command='sh clock', verbose=True))
    Вызываем send_show_command
    Позиционные аргументы: ({'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'},)
    Ключевые аргументы: {'command': 'sh clock'}
    *15:10:09.222 UTC Fri Oct 18 2019

    In [7]: print(send_show_command(params=device_params, command='sh clock', verbose=True))
    Вызываем send_show_command
    Ключевые аргументы: {'params': {'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'command': 'sh clock'}
    *15:10:28.524 UTC Fri Oct 18 2019

    In [8]: print(send_show_command(device_params, 'sh clock', verbose=False))
    *14:01:18.141 UTC Mon Feb 26 2018


Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.


Задание 7.4
~~~~~~~~~~~

Создать декоратор retry, который выполняет декорируемую функцию повторно,
заданное количество раз, если результат функции не был истинным.

Пример работы декоратора:

.. code:: python

    In [2]: @retry(times=3)
        ..: def send_show_command(device, show_command):
        ..:     print('Подключаюсь к', device['ip'])
        ..:     try:
        ..:         with ConnectHandler(**device) as ssh:
        ..:             ssh.enable()
        ..:             result = ssh.send_command(show_command)
        ..:         return result
        ..:     except SSHException:
        ..:         return None
        ..:

    In [3]: send_show_command(device_params, 'sh clock')
    Подключаюсь к 192.168.100.1
    Out[3]: '*14:22:01.566 UTC Mon Mar 5 2018'

    In [4]: device_params['password'] = '123123'

    Обратите внимание, что если указано, что повторить попытку надо 3 раза,
    то это три раза в дополнение к первому, то есть все подключение будет 4 раза:
    In [5]: send_show_command(device_params, 'sh clock')
    Подключаюсь к 192.168.100.1
    Подключаюсь к 192.168.100.1
    Подключаюсь к 192.168.100.1
    Подключаюсь к 192.168.100.1

Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.

Задание 7.4a
~~~~~~~~~~~

Переделать декоратор retry из задания 7.4: добавить параметр delay,
который контролирует через какое количество секунд будет выполняться повторная попытка.

Пример работы декоратора:

.. code:: python

    In [2]: @retry(times=3, delay=5)
        ..: def send_show_command(device, show_command):
        ..:     print('Подключаюсь к', device['ip'])
        ..:     try:
        ..:         with ConnectHandler(**device) as ssh:
        ..:             ssh.enable()
        ..:             result = ssh.send_command(show_command)
        ..:         return result
        ..:     except (NetMikoAuthenticationException, NetMikoTimeoutException):
        ..:         return None
        ..:

    In [3]: send_show_command(device_params, 'sh clock')
    Подключаюсь к 192.168.100.1
    Out[4]: '*16:35:59.723 UTC Fri Oct 18 2019'

    In [5]: device_params['password'] = '123123'

    In [6]: send_show_command(device_params, 'sh clock')
    Подключаюсь к 192.168.100.1
    Повторное подключение через 5 сек
    Подключаюсь к 192.168.100.1
    Повторное подключение через 5 сек
    Подключаюсь к 192.168.100.1
    Повторное подключение через 5 сек
    Подключаюсь к 192.168.100.1


Тест берет значения из словаря device_params в этом файле, поэтому если
для заданий используются другие адреса/логины, надо заменить их в словаре.


Задание 7.5
~~~~~~~~~~~

Создать декоратор count_calls, который считает сколько раз декорируемая функция была вызвана.
При вызове функции должно отображаться количество вызовов этой функции.

Пример работы декоратора:

.. code:: python

    In [11]: @count_calls
        ...: def f1():
        ...:     return True
        ...:

    In [12]: @count_calls
        ...: def f2():
        ...:     return False
        ...:

    In [14]: for _ in range(5):
        ...:     f1()
        ...:
    Всего вызовов: 1
    Всего вызовов: 2
    Всего вызовов: 3
    Всего вызовов: 4
    Всего вызовов: 5

    In [15]: for _ in range(5):
        ...:     f2()
        ...:
    Всего вызовов: 1
    Всего вызовов: 2
    Всего вызовов: 3
    Всего вызовов: 4
    Всего вызовов: 5

    In [16]: for _ in range(5):
        ...:     f1()
        ...:
    Всего вызовов: 6
    Всего вызовов: 7
    Всего вызовов: 8
    Всего вызовов: 9
    Всего вызовов: 10


Задание 7.5a
~~~~~~~~~~~

Переделать декоратор count_calls из задания 7.5.
Вместо вывода количества вызовов на стандартный поток вывода,
надо записать его в атрибут total_calls.

Пример работы декоратора:

.. code:: python

    In [10]: @count_calls
        ...: def f1():
        ...:     return False
        ...:

    In [11]: @count_calls
        ...: def f2():
        ...:     return False
        ...:

    In [12]: for _ in range(5):
        ...:     f1()
        ...:

    In [13]: for _ in range(5):
        ...:     f2()
        ...:

    In [14]: for _ in range(5):
        ...:     f1()
        ...:

    In [15]: f1.total_calls
    Out[15]: 10

    In [16]: f2.total_calls
    Out[16]: 5



Задание 7.6
~~~~~~~~~~~

Создать декоратор total_order, который добавляет к классу методы:

* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


Декоратор total_order полагается на то, что в классе уже определены методы:

* __eq__ - операция ==
* __lt__ - операция <

Если методы __eq__ и __lt__ не определены, сгенерировать исключение ValueError при декорации.

Проверить работу декоратора можно на примере класса IPAddress. Определение класса нельзя менять, можно только декорировать.
Декоратор не должен использовать переменные класса IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
Декоратор должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.


Пример проверки методов с классом IPAddress после декорирования:

.. code:: python

    In [4]: ip1 = IPAddress('10.10.1.1')

    In [5]: ip2 = IPAddress('10.2.1.1')

    In [6]: ip1 < ip2
    Out[6]: False

    In [7]: ip1 > ip2
    Out[7]: True

    In [8]: ip1 >= ip2
    Out[8]: True

    In [9]: ip1 <= ip2
    Out[9]: False

    In [10]: ip1 == ip2
    Out[10]: False

    In [11]: ip1 != ip2
    Out[11]: True

