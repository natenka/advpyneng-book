Функции первого класса
----------------------

В Python все функции являются объектами первого класса. Это означает, что Python поддерживает:

* передачу функций в качестве аргументов другим функциям
* возвращение функции как результата других функций
* присваивание функций переменным
* сохранение функций в структурах данных


Например, первый пункт "передача функций в качестве аргументов другим функциям" встречается
при использовании встроенной функции map. Тут map применяет функцию str к каждому элементу списка:

.. code:: python

    In [1]: list(map(str, [1, 2, 3]))
    Out[1]: ['1', '2', '3']

Функция delay ожидает как аргумент задержку в секундах, другую функцию и ее аргументы:

.. code:: python

    In [2]: import time

    In [3]: def delay(seconds, func, *args, **kwargs):
       ...:     print(f'Delay {seconds} seconds...')
       ...:     time.sleep(seconds)
       ...:     return func(*args, **kwargs)
       ...:


Теперь функции delay можно передавать любую другую функцию как аргумент и
она выполнится после указанной паузы:

.. code:: python

    In [4]: def summ(a, b):
       ...:     return a + b
       ...:

    In [5]: delay(5, summ, 1, 4)
    Delay 5 seconds...
    Out[5]: 5

Сохранение функций в структурах данных:

.. code:: python

    In [8]: functions = [delay, summ]

    In [9]: functions
    Out[9]:
    [<function __main__.delay(seconds, func, *args, **kwargs)>,
     <function __main__.summ(a, b)>]

Присваивание функций переменным:

.. code:: python

    In [10]: delay_execution = delay

    In [11]: delay_execution
    Out[11]: <function __main__.delay(seconds, func, *args, **kwargs)>

    In [12]: delay_execution(5, summ, 1, 4)
    Delay 5 seconds...
    Out[12]: 5

