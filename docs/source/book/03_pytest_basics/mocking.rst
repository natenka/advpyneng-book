Подделка функций (Mocking)
--------------------------

Код

.. code:: python

    import getpass

    def check_passwd(min_length=8, check_username=True):
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True

Тест:

.. code:: python

    from check_password_function_input import check_passwd


    def test_password_min_length():
        assert check_passwd(min_length=3)

Результат:

::

    $ pytest test_check_password_input.py
    ======================= test session starts ========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 1 item

    test_check_password_input.py F                               [100%]

    ============================= FAILURES =============================
    _____________________ test_password_min_length _____________________

        def test_password_min_length():
    >       assert check_passwd(min_length=3)

    test_check_password_input.py:5:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    check_password_function_input.py:2: in check_passwd
        username = input('Username: ')
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <_pytest.capture.DontReadFromInput object at 0xb68f424c>
    args = ()

        def read(self, *args):
    >       raise IOError("reading from stdin while output is captured")
    E       OSError: reading from stdin while output is captured

    /home/vagrant/venv/pyneng-py3-7/lib/python3.7/site-packages/_pytest/capture.py:706: OSError
    ----------------------- Captured stdout call -----------------------
    Username:
    ======================== 1 failed in 0.09s =========================

monkeypatch
~~~~~~~~~~~


.. code:: python

    from check_password_function_input import check_passwd


    def test_password_min_length(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x=None: 'nata')
        monkeypatch.setattr('getpass.getpass', lambda x=None: '12345')
        assert check_passwd(min_length=3)


Проверка

::

    $ pytest test_check_password_input.py
    ======================= test session starts ========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 1 item

    test_check_password_input.py .                               [100%]

    ======================== 1 passed in 0.03s =========================

Проверка нескольких сценариев с parametrize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    import pytest
    from check_password_function_input import check_passwd


    @pytest.mark.parametrize("username,password,result",[
        ('nata', '12345', True),
        ('nata', '12345nata', False)
    ])
    def test_password_min_length(monkeypatch,
                                 username, password, result):
        monkeypatch.setattr('builtins.input', lambda x=None: username)
        monkeypatch.setattr('getpass.getpass', lambda x=None: password)
        assert result == check_passwd(min_length=3)

Проверка:

::

    $ pytest test_check_password_input.py
    ======================= test session starts ========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 2 items

    test_check_password_input.py ..                              [100%]

    ======================== 2 passed in 0.03s =========================
