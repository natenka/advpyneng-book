conftest
--------

conftest.py это файл в котором хранятся fixture для разных тестов.
Этих файлов может быть много, например, может быть такая структура:

::

    ├── conftest.py
    ├── pytest.ini
    └── tests
        ├── conftest.py
        ├── helper_test_functions.py
        ├── network
        │   ├── conftest.py
        │   └── test_11_network_fixture_params.py
        └── unit
            ├── conftest.py
            ├── test_01_check_ip.py
            ├── test_02_send_command.py
            ├── test_03_check_password.py
            ├── test_04_get_interfaces.py
            ├── test_05_class_topology.py
            └── test_06_class_ipv4network.py


Conftest.py также добавляет каталог в котором он находится в sys.path.
Поэтому часто можно встретить пустые файлы conftest.py.
Например в этом случае conftest.py в текущем каталоге может быть пустым,
но он нужен чтобы тесты из каталога tests могли импортировать функции из файлов
в текущем каталоге:

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
        ├── conftest.py
        ├── test_check_ip_function.py
        ├── test_check_password_input.py
        ├── test_check_password_parametrize.py
        ├── test_check_password.py
        └── test_ipv4_network.py

