Рекомендации/нюансы по тестам
-----------------------------

Много assert в тесте
~~~~~~~~~~~~~~~~~~~~

Чем плохо то, что в тесте много assert - тест остановится на первом assert, который не
прошел и не будет проверять другие.

.. note::

    Есть плагины, которые позволяют в каком-то виде проверять все assert
    (или выражения, которые используются вместо assert в плагине).

В идеале было бы хорошо, чтобы в каждом тесте был только один assert, но так
далеко не всегда есть смысл делать.

Иногда по одному результату есть много проверок. И вам может подходить то, что если
одна проверка не прошла, другие не выполняются.
Пример `теста scrapli в котором много assert <https://github.com/carlmontanari/scrapli/blob/master/tests/unit/test_factory.py#L145>`__:

.. code:: python

    @pytest.mark.parametrize(
        "test_data",
        [(Scrapli, "system", NetworkDriver), (AsyncScrapli, "asyncssh", AsyncNetworkDriver)],
        ids=["sync_factory", "async_factory"],
    )
    def test_factory_community_platform_variant(test_data):
        Factory, transport, expected_driver = test_data
        driver = Factory(
            platform="scrapli_networkdriver",
            host="localhost",
            variant="test_variant1",
            transport=transport,
        )
        assert isinstance(driver, expected_driver)
        assert driver.transport_name == transport
        assert driver.failed_when_contains == [
            "% Ambiguous command",
            "% Incomplete command",
            "% Invalid input detected",
            "% Unknown command",
        ]
        assert driver.textfsm_platform == "cisco_iosxe"
        assert driver.genie_platform == "iosxe"
        assert driver.default_desired_privilege_level == "configuration"
        assert callable(driver.on_open)
        assert callable(driver.on_close)
        for actual_priv_level, expected_priv_level in zip(
            driver.privilege_levels.values(), TEST_COMMUNITY_PRIV_LEVELS.values()
        ):
            assert actual_priv_level.name == expected_priv_level.name
            assert actual_priv_level.pattern == expected_priv_level.pattern

Циклы в тестах
~~~~~~~~~~~~~~

Циклы в тестах во многом попадают в ту же категорию, что и много assert.
Однако стоит учитывать, что, если, например, в тесте проверяется подключение к
нескольким устройствам в цикле и assert стоит именно в цикле по устройствам,
то достаточно одному устройству не пройти assert и к остальным тест подключаться
не будет. Иногда это может быть то, что нужно от теста, иногда нет.

Правильный результат в fixture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Правильный результат, который должна была вернуть функция/метод/класс, очень часто
пишется прямо в тесте (correct_access_dict, correct_trunk_dict).

.. code:: python

    import pytest


    @pytest.fixture
    def cfg_example_1():
        cfg = (
            "!\n"
            "interface FastEthernet0/0\n"
            " switchport mode access\n"
            " switchport access vlan 10\n"
            "!\n"
            "interface FastEthernet0/1\n"
            " switchport trunk encapsulation dot1q\n"
            " switchport trunk allowed vlan 100,200\n"
            " switchport mode trunk\n"
            "!\n"
            "interface FastEthernet0/2\n"
            " switchport mode access\n"
            " switchport access vlan 20\n"
            "!\n"
        )
        return cfg


    def test_cfg_1(cfg_example_1):
        correct_access_dict = {"FastEthernet0/0": 10, "FastEthernet0/2": 20}
        correct_trunk_dict = {"FastEthernet0/1": [100, 200]}
        access_dict, trunk_dict = get_int_vlan_map(cfg_example_1)
        assert access_dict == correct_access_dict and trunk_dict == correct_trunk_dict

Иногда результат слишком большой чтобы писать в тесте,
тогда можно встретить варианты с записью параметров и результатов в файлах/структурах данных.
Также часто наборы входящих параметров и результатов пишут в parametrize:

.. code:: python

    @pytest.mark.parametrize(
        "network,correct_net_len",
        [
            ("10.1.1.192/30", 2),
            ("10.1.1.0/28", 14),
            ("10.1.1.0/24", 254),
        ],
    )
    def test_len_method(network, correct_net_len):
        network = Network(network)
        assert hasattr(network, "__len__")
        assert len(network) == correct_net_len, "Метод __len__ возвращает неверное значение"

Fixture, как правило, используются только для подготовки данных или подготовки до теста и
удаления после теста, но не для передачи правильного результата в тест.


Проверка типов данных
~~~~~~~~~~~~~~~~~~~~~

В тестах можно проверять типы данных, которые возвращает функция/метод/класс,
но обычно это делают не от и до, например, по всем данным словаря, а только проверяют
что это словарь.
Как правило, проверка типа делается чтобы ошибка была понятной, что возвращается
не тот тип данных.
При этом, например, не нужно проверять каждый элемент словаря, потому что
при сравнении словарь == правильный словарь, все отличия покажет pytest


.. code:: python

    def test_1():
        correct_dict = {"FastEthernet0/0": 10, "FastEthernet0/2": 20}
        result_dict = {"FastEthernet0/0": "10", "FastEthernet0/2": "20"}
        assert result_dict == correct_dict

Пример вывода:

::

        def test_1():
            correct_dict = {"FastEthernet0/0": 10, "FastEthernet0/2": 20}
            result_dict = {"FastEthernet0/0": "10", "FastEthernet0/2": "20"}
    >       assert result_dict == correct_dict
    E       AssertionError: assert {'FastEtherne...net0/2': '20'} == {'FastEtherne...ernet0/2': 20}
    E         Differing items:
    E         {'FastEthernet0/0': '10'} != {'FastEthernet0/0': 10}
    E         {'FastEthernet0/2': '20'} != {'FastEthernet0/2': 20}
    E         Use -v to get the full diff


Вывод с -v:

::

        def test_1():
            correct_dict = {"FastEthernet0/0": 10, "FastEthernet0/2": 20}
            result_dict = {"FastEthernet0/0": "10", "FastEthernet0/2": "20"}
    >       assert result_dict == correct_dict
    E       AssertionError: assert {'FastEtherne...net0/2': '20'} == {'FastEtherne...ernet0/2': 20}
    E         Differing items:
    E         {'FastEthernet0/2': '20'} != {'FastEthernet0/2': 20}
    E         {'FastEthernet0/0': '10'} != {'FastEthernet0/0': 10}
    E         Full diff:
    E         - {'FastEthernet0/0': 10, 'FastEthernet0/2': 20}
    E         + {'FastEthernet0/0': '10', 'FastEthernet0/2': '20'}
    E         ?                     +  +                     +  +


Проверка True/False
~~~~~~~~~~~~~~~~~~~

Стоит ли писать в тестах  ``if value == True`` вместо ``if value``?

Если это проверка типа isinstance, например, то не надо:

.. code:: python

    assert isinstance(value, str)

Если это проверка именно того что возвращает функция, которую мы тестируем,
то ``== True`` более явно говорит, что тут должен быть результат именно True,
а не любой истинный результат

.. code:: python

    assert function(value) == True

.. note::

    Речь только о тестах, для кода в целом рекомендация писать
    ``if value`` не ``if value == True``

Закрытие сессий/файлов в тесте
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Два примера кода. Первый - сессия закрывается close:

.. code:: python

    def test_telnet_class(reachable_device):
        r1 = CiscoTelnet(**reachable_device)
        assert r1.prompt == ">"
        r1.close()

Второй - сессия закрывает в менеджере контекста:

.. code:: python

    def test_telnet_class(reachable_device):
        with CiscoTelnet(**reachable_device) as r1:
            assert r1.prompt == ">"


Очень важная разница этих вариантов в том, что менеджер контекста закроет
сессию даже если assert не прошел, а close НЕ сработает.

При этом первый пример можно переделать так и тогда сессия закроется
(но лучше конечно использовать менеджер контекста где возможно или fixture):

.. code:: python

    def test_telnet_class(reachable_device):
        r1 = CiscoTelnet(**reachable_device)
        r1_prompt = r1.prompt
        r1.close()
        assert r1_prompt == ">"


Структура теста
~~~~~~~~~~~~~~~

`AAA (Arrange, Act, Assert) <https://docs.pytest.org/en/latest/explanation/anatomy.html#test-anatomy>`__.

Тесты, как правило, можно разбить на несколько этапов:

* Arrange
* Act
* Assert
* Cleanup

При этом тест можно состоять только из первых трех шагов, если стадия cleanup
не нужна.

Как правило, в pytest стадии Arrange и Cleanup делаются в fixture, а остальное в тесте.
