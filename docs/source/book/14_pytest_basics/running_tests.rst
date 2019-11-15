Запуск тестов
-------------

Запуск тестов из конкретного файла:

::

    $ pytest test_check_password.py
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py ...                                        [100%]

    =========================== 3 passed in 0.02s ===========================


Запуск всех тестов:

::

    $ pytest
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 9 items

    test_check_ip_function.py .                                       [ 11%]
    test_check_password.py ...                                        [ 44%]
    test_ipv4_network.py .....                                        [100%]

    =========================== 9 passed in 0.07s ===========================

Запуск тестов с более подробной информацией:

::

    $ pytest -v
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0 -- /home/vagrant/venv/pyneng-py3-7/bin/python3.7
    cachedir: .pytest_cache
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 9 items

    test_check_ip_function.py::test_check_ip PASSED                   [ 11%]
    test_check_password.py::test_password_min_length PASSED           [ 22%]
    test_check_password.py::test_password_contains_username PASSED    [ 33%]
    test_check_password.py::test_password_default_values PASSED       [ 44%]
    test_ipv4_network.py::test_class_created PASSED                   [ 55%]
    test_ipv4_network.py::test_attributes_created PASSED              [ 66%]
    test_ipv4_network.py::test_methods_created PASSED                 [ 77%]
    test_ipv4_network.py::test_return_types PASSED                    [ 88%]
    test_ipv4_network.py::test_address_allocation PASSED              [100%]

    =========================== 9 passed in 0.08s ===========================

Запуск одного теста

::

    $ pytest test_check_password.py::test_password_min_length -v
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0 -- /home/vagrant/venv/pyneng-py3-7/bin/python3.7
    cachedir: .pytest_cache
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 1 item

    test_check_password.py::test_password_min_length PASSED           [100%]

    =========================== 1 passed in 0.01s ===========================

Отображение вывода на stdout:

::

    $ pytest test_check_password.py -s
    =========================== test session starts ============================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py Проверяем пароль
    Пароль для пользователя nata прошел все проверки
    Пароль содержит имя пользователя
    .Пароль для пользователя nata прошел все проверки
    Пароль содержит имя пользователя
    .Пароль слишком короткий
    Пароль содержит имя пользователя
    Пароль для пользователя nata прошел все проверки
    .

    ============================ 3 passed in 0.02s =============================

Аналогично с verbose:

::

    $ pytest test_check_password.py -v -s
    =========================== test session starts ============================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0 -- /home/vagrant/venv/pyneng-py3-7/bin/python3.7
    cachedir: .pytest_cache
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py::test_password_min_length Проверяем пароль
    Пароль для пользователя nata прошел все проверки
    Пароль содержит имя пользователя
    PASSED
    test_check_password.py::test_password_contains_username Пароль для пользователя nata прошел все проверки
    Пароль содержит имя пользователя
    PASSED
    test_check_password.py::test_password_default_values Пароль слишком короткий
    Пароль содержит имя пользователя
    Пароль для пользователя nata прошел все проверки
    PASSED

    ============================ 3 passed in 0.02s =============================

Когда тесты не проходят
~~~~~~~~~~~~~~~~~~~~~~~

Вывод когда тесты не проходят

::

    $ pytest test_check_password.py
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py .F.                                        [100%]

    =============================== FAILURES ================================
    ____________________ test_password_contains_username ____________________

        def test_password_contains_username():
            assert check_passwd('nata', '12345nata', min_length=3, check_username=False)
            assert not check_passwd('nata', '12345nata', min_length=3, check_username=True)
    >       assert not check_passwd('nata', '12345NATA', min_length=3, check_username=True), "Если в пароле присутствует имя пользователя в любом регистре, проверка не должна пройти"
    E       AssertionError: Если в пароле присутствует имя пользователя в любом регистре, проверка не должна пройти
    E       assert not True
    E        +  where True = check_passwd('nata', '12345NATA', min_length=3, check_username=True)

    test_check_password.py:12: AssertionError
    ------------------------- Captured stdout call --------------------------
    Пароль для пользователя nata прошел все проверки
    Пароль содержит имя пользователя
    Пароль для пользователя nata прошел все проверки

Короткий вывод traceback:

::

    $ pytest test_check_password.py --tb=line
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py .F.                                        [100%]

    =============================== FAILURES ================================
    /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics/test_check_password.py:12: AssertionError: Если в пароле присутствует имя пользователя в любом регистре, проверка не должна пройти
    ====================== 1 failed, 2 passed in 0.07s ======================


Остановиться после первого неудачного теста
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pytest test_check_password.py --tb=line -x
    ========================== test session starts ==========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 3 items

    test_check_password.py .F

    =============================== FAILURES ================================
    /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics/test_check_password.py:12: AssertionError: Если в пароле присутствует имя пользователя в любом регистре, проверка не должна пройти
    ====================== 1 failed, 1 passed in 0.06s ======================


Показать какие тесты есть, но не запускать их
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pytest --collect-only
    ========================== test session starts ===========================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 9 items
    <Module test_check_ip_function.py>
      <Function test_check_ip>
    <Module test_check_password.py>
      <Function test_password_min_length>
      <Function test_password_contains_username>
      <Function test_password_default_values>
    <Module test_ipv4_network.py>
      <Function test_class_created>
      <Function test_attributes_created>
      <Function test_methods_created>
      <Function test_return_types>
      <Function test_address_allocation>

    ========================= no tests ran in 0.05s ==========================
