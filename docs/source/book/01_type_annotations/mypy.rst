Основы mypy
-----------

Пример запуска скрипта с помощью mypy:

::

    $ mypy example_01_function_check_ip.py
    example_01_function_check_ip.py:13: error: Argument 1 to "check_ip" has incompatible type "int"; expected "str"
    Found 1 error in 1 file (checked 1 source file)

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

