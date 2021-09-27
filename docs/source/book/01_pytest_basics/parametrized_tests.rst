Параметризация теста
--------------------


Очень часто в тестах нужно проверять функцию/класс/метод на разных входящих данных.
Один вариант, в этом случае, будет написать несколько assert в одном тесте.

.. code:: python

    def check_passwd(username, password, min_length=8, check_username=True):
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True


    def test_password_min_length():
        assert check_passwd('user', '12345', min_length=3) == True
        assert check_passwd('user', '123456', min_length=5) == False
        assert check_passwd('user', 'userpass', min_length=5) == False

Этот вариант плох тем, что теперь все три проверки считаются одним тестом и
если одна из проверок не проходит, следующие не проверяются.

Параметризация тестов позволяет указать несколько наборов данных, на которых надо
проверить тест:

.. code:: python

    import pytest


    @pytest.mark.parametrize(
        ("user", "passwd", "min_len", "result"),
        [
            ("user1", "123456", 4, True),
            ("user1", "123456", 8, False),
            ("user1", "123456", 6, True),
        ],
    )
    def test_min_len_param(user, passwd, min_len, result):
        assert check_passwd(user, passwd, min_length=min_len) == result

и, что особенно удобно, каждый набор данных срабатывает как отдельный
запуск теста:

.. code::

    $ pytest test_check_password.py -v
    ============================ test session starts ==============================
    ...
    collected 3 items

    test_check_password.py::test_min_len_param[user1-123456-4-True] PASSED   [ 33%]
    test_check_password.py::test_min_len_param[user1-123456-8-False] PASSED  [ 66%]
    test_check_password.py::test_min_len_param[user1-123456-6-True] PASSED   [100%]

    ============================= 3 passed in 0.03s ================================

Пример использования параметризации теста для одного параметра:

.. code:: python

    import ipaddress


    def is_ip_address(ip):
        if not isinstance(ip, str):
            return False
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False


    @pytest.mark.parametrize("ip", ["10.1.1.1", "224.1.1.1", "0.0.0.0"])
    def test_is_ip_address_correct(ip):
        assert is_ip_address(ip) == True


    @pytest.mark.parametrize("ip", ["500.1.1.1", "50.1.1", "a", 100])
    def test_is_ip_address_wrong(ip):
        assert is_ip_address(ip) == False


Запуск теста:

.. code::
    $ pytest test_check_ip.py
    ========================= test session starts =======================
    ...
    collected 9 items

    test_check_ip.py::test_check_ip PASSED                          [ 11%]
    test_check_ip.py::test_check_ip_correct[10.1.1.1] PASSED        [ 22%]
    test_check_ip.py::test_check_ip_correct[224.1.1.1] PASSED       [ 33%]
    test_check_ip.py::test_check_ip_correct[0.0.0.0] PASSED         [ 44%]
    test_check_ip.py::test_check_ip_wrong[500.1.1.1] PASSED         [ 55%]
    test_check_ip.py::test_check_ip_wrong[50.1.1] PASSED            [ 66%]
    test_check_ip.py::test_check_ip_wrong[a] PASSED                 [ 77%]
    test_check_ip.py::test_check_ip_wrong[100] PASSED               [ 88%]
    test_check_ip.py::test_check_ip_wrong[ip4] PASSED               [100%]

