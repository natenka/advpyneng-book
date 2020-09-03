Основы mypy
-----------

Так как сам Python никак не проверяет указанные типы данных, надо использовать какой-то дополнительный
модуль для проверки. Один из таких модулей - mypy.

Mypy выполняет статический анализ кода - проверяет соответствие типов данных без выполнения кода.

.. note::

    Mypy не единственный проект такого типа. Другие модули: pyre, pytype.


Пример запуска скрипта с помощью mypy:

::

    $ mypy example_01_function_check_ip.py
    example_01_function_check_ip.py:13: error: Argument 1 to "check_ip" has incompatible type "int"; expected "str"
    Found 1 error in 1 file (checked 1 source file)


Писать аннотацию для переменных нужно далеко не всегда. Как правило, того типа который
"угадал" mypy достаточно. Например, в этом случае mypy понимает, что ip это строка:

.. code:: python

    ip = '10.1.1.1'

И не будет выводить никаких ошибок:

::

    $ mypy example_03_variable.py

    Success: no issues found in 1 source file

Однако, если переменная может быть и строкой и числом:

.. code:: python

    ip = '10.1.1.1'
    ip = 3

mypy посчитает это ошибкой:

::

    example_03_variable.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")
    Found 1 error in 1 file (checked 1 source file)

В таком случае надо явно указать, что переменная может быть числом или строкой:

.. code:: python

    from typing import Union

    ip: Union[int, str] = '10.1.1.1'
    ip = 3




strict
~~~~~~


.. code:: python

    def func1(a: str, b: str) -> str:
        return a + b

    def func2(c, d):
        result = func1(4, 6)
        return c + d

По умолчанию, mypy игнорирует функции без аннотации типов:

::

    $ mypy testme.py
    Success: no issues found in 1 source file

С параметром strict mypy проверяет эти функции и их работу с другими объектами:

::

    $ mypy testme.py --strict
    testme.py:4: error: Function is missing a type annotation
    testme.py:5: error: Argument 1 to "func1" has incompatible type "int"; expected "str"
    testme.py:5: error: Argument 2 to "func1" has incompatible type "int"; expected "str"
    Found 3 errors in 1 file (checked 1 source file)


reveal
~~~~~~

reveal_type


reveal_locals:

.. code:: python

    def check_passwd(username: str, password: str,
                     min_length: int = 8, check_username: bool = True) -> bool:
        reveal_locals()
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True

::

    example_02_function_check_passwd.py:4: note: Revealed local types are:
    example_02_function_check_passwd.py:4: note:     check_username: builtins.bool
    example_02_function_check_passwd.py:4: note:     min_length: builtins.int
    example_02_function_check_passwd.py:4: note:     password: builtins.str
    example_02_function_check_passwd.py:4: note:     username: builtins.str

