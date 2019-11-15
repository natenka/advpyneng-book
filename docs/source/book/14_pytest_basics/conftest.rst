conftest
--------

::

    $ tree
    .
    ├── check_ip_functions.py
    ├── check_password_function_input.py
    ├── check_password_function.py
    ├── class_ipv4_network.py
    ├── common_functions.py
    ├── conftest.py
    └── tests
        ├── test_check_ip_function.py
        ├── test_check_password_input.py
        ├── test_check_password_parametrize.py
        ├── test_check_password.py
        └── test_ipv4_network.py

Запуск тестов:

::

    $ pytest
    ============================= test session starts =============================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 0 items / 5 errors

    =================================== ERRORS ====================================
    ______________ ERROR collecting tests/test_check_ip_function.py _______________
    ImportError while importing test module '/home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics/tests/test_check_ip_function.py'.
    Hint: make sure your test modules/packages have valid Python names.
    Traceback:
    tests/test_check_ip_function.py:1: in <module>
        from check_ip_functions import check_ip
    E   ModuleNotFoundError: No module named 'check_ip_functions'
    !!!!!!!!!!!!!!!!!!! Interrupted: 5 errors during collection !!!!!!!!!!!!!!!!!!!
    ============================== 5 error in 0.18s ===============================


Достаточно создать пустой файл conftest.py и тесты заработают

::

    $ touch conftest.py
    $ pytest
    ============================= test session starts =============================
    platform linux -- Python 3.7.3, pytest-5.2.0, py-1.8.0, pluggy-0.12.0
    rootdir: /home/vagrant/repos/advanced-pyneng-1/advpyneng-online-oct-nov-2019/examples/14_pytest_basics
    collected 13 items

    tests/test_check_ip_function.py .                                       [  7%]
    tests/test_check_password.py ...                                        [ 30%]
    tests/test_check_password_input.py ..                                   [ 46%]
    tests/test_check_password_parametrize.py ..                             [ 61%]
    tests/test_ipv4_network.py .....                                        [100%]

    ============================= 13 passed in 0.09s ==============================
